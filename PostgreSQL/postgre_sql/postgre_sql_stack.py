from aws_cdk import (
  aws_iam as iam,
  aws_rds as rds,
  aws_sqs as sqs,
  aws_sns as sns,
  aws_ec2 as ec2,
  aws_s3  as s3,
  aws_logs as logs,
  aws_kms as kms,
  aws_cloudwatch         as cloudwatch,
  aws_cloudwatch_actions as cloudwatch_actions,
  aws_secretsmanager    as secretsmanager,
  aws_s3_notifications  as s3n,
  aws_sns_subscriptions as subs,
  aws_lambda            as lfn,
  Aspects, CfnOutput, Stack, SecretValue, Tags, Fn, Aws, CfnMapping, Duration, RemovalPolicy,
  App, RemovalPolicy
)

from constructs import Construct

import json

import os
from dotenv import load_dotenv

load_dotenv(override=True)

def tagResource(resource, name:str):

    owner = os.getenv("OWNER","")
    application = os.getenv("APPLICATION","")
    environment = os.getenv("ENVIRONMENT","")
    administrator_email = os.getenv("ADMINISTRATOR_EMAIL","")

    Tags.of(resource).add("Owner", owner)
    Tags.of(resource).add("Application", application)
    Tags.of(resource).add("Name", name)
    Tags.of(resource).add("Environment", environment)
    Tags.of(resource).add("AdministratorEmail", administrator_email)


class PostgreSqlStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        cidr = os.getenv ("CIDR" , "")
        db_name = os.getenv ("DB_NAME" , "")
        vpc_id = os.getenv ("VPC_ID" , "")
        az = os.getenv ("AZA" , "")
        subnet_id_a = os.getenv ("SUBNETA" , "")
        subnet_id_b = os.getenv ("SUBNETB" , "")

        # The code that defines your stack goes here

        secret_db_creds = secretsmanager.Secret(
            self,
            "secret_db_creds",
            secret_name="hrs/db_creds",
            description =db_name + "PostgreSQL Credentials",
            generate_secret_string=secretsmanager.SecretStringGenerator(
                secret_string_template=json.dumps({"username": "hrs"}),
                exclude_punctuation=True,
                generate_string_key="password",
            ),
        )

        vpc_hrs = ec2.Vpc.from_lookup(self, 'VPC',  vpc_id=vpc_id)

        # vpc_hrs = ec2.Vpc(
        #     self,
        #     "vpc_hrs",
        #     max_azs=3,
        #     ip_addresses=ec2.IpAddresses.cidr(cidr),
        #     subnet_configuration=[
        #         ec2.SubnetConfiguration(
        #             subnet_type=ec2.SubnetType.PUBLIC,
        #             name="Public",
        #             cidr_mask=26
        #         ),
        #         ec2.SubnetConfiguration(
        #             subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
        #             name="Private",
        #             cidr_mask=26
        #         ),
        #     ],
        #     nat_gateways=1,
        # )


        subnetid_a = ec2.Subnet.from_subnet_attributes(self,'subnetid_a', availability_zone = az, subnet_id = subnet_id_a)
        subnetid_b = ec2.Subnet.from_subnet_attributes(self,'subnetid_b', availability_zone = az, subnet_id = subnet_id_b)

        vpc_subnets_selection = ec2.SubnetSelection(subnets = [subnetid_a, subnetid_b])

        subnet_group_hrs = rds.SubnetGroup(
            self,
            "subnet_group_hrs",
            vpc=vpc_hrs,
            # vpc_subnets=ec2.SubnetSelection(
            #     subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS
            # ),
            vpc_subnets = vpc_subnets_selection,
            subnet_group_name="hrs-postgres-subnet-group",
            description="Subnet group for hrs postgres",
        )

        security_group_hrs_db = ec2.SecurityGroup(
            self,
            "security_group_hrs_db",
            vpc=vpc_hrs,
            security_group_name="security_group_hrs_db",
            allow_all_outbound=True,
        )

        security_group_hrs_db.add_ingress_rule(
            peer=ec2.Peer.ipv4(vpc_hrs.vpc_cidr_block),
            connection=ec2.Port.tcp(5432),
        )

        role_enhanced_monitoring = iam.Role(
            self,
            "role_enhanced_monitoring",
            assumed_by=iam.ServicePrincipal("monitoring.rds.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "service-role/AmazonRDSEnhancedMonitoringRole"
                ),
            ],
            role_name="rds_enhanced_monitoring",
        )

        parameter_group_postgres = rds.ParameterGroup(
            self,
            "parameter_group_postgres",
            engine=rds.DatabaseInstanceEngine.postgres(
                version=rds.PostgresEngineVersion.VER_15
            ),
            parameters={
                "max_standby_streaming_delay": "600000",  # milliseconds (5 minutes)
                "max_standby_archive_delay": "600000",  # milliseconds (5 minutes)
            },
        )

        self.rds_db_postgres = rds.DatabaseInstance(
            self,
            "rds_db_postgres",
            instance_identifier="hrs-postgres",
            engine=rds.DatabaseInstanceEngine.postgres(
                version=rds.PostgresEngineVersion.VER_15
            ),
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.M5, ec2.InstanceSize.LARGE
            ),
            parameter_group=parameter_group_postgres,
            allocated_storage=30,
            max_allocated_storage=30,
            credentials=rds.Credentials.from_secret(secret_db_creds),
            database_name=db_name,
            vpc=vpc_hrs,
            subnet_group=subnet_group_hrs,
            enable_performance_insights=True,
            performance_insight_retention=rds.PerformanceInsightRetention.DEFAULT,
            monitoring_interval=Duration.seconds(60),
            publicly_accessible=False,
            monitoring_role=role_enhanced_monitoring,
            backup_retention=Duration.days(7),
            security_groups=[
                security_group_hrs_db,
            ],
            allow_major_version_upgrade=True, 
            iam_authentication=True,
        )

        tagResource(self.rds_db_postgres, name=db_name)

        pub_subnet_id_a = os.getenv("PUB_SUBNETA","")
        pub_subnetid_a = ec2.Subnet.from_subnet_attributes(self,'pub_subnetid_a', availability_zone = az, subnet_id = pub_subnet_id_a)
        vpc_pub_subnet_selection = ec2.SubnetSelection(subnets = [pub_subnetid_a])


        # Create Bastion
        key_name = os.getenv ("KEY_NAME" , "")
        bastion = ec2.BastionHostLinux(self, "postgresql-bastion-host",
                                       vpc=vpc_hrs,
                                       subnet_selection=vpc_pub_subnet_selection,
                                       instance_name="postgresql-bastion-host",
                                       instance_type=ec2.InstanceType(instance_type_identifier="t2.micro"))

        # Setup key_name for EC2 instance login if you don't use Session Manager
        bastion.instance.instance.add_property_override("KeyName", key_name)


        bastion_allowed_cidr = os.getenv("BASTION_ALLOWED_CIDR","")
        bastion.allow_ssh_access_from(ec2.Peer.ipv4(bastion_allowed_cidr))

        tagResource(bastion, name="postgresql-bastion-host")
