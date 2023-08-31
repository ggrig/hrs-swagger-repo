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

####################################

class PostgreSqlStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, 
                db_name:str,                ## database name
                 **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "PostgreSqlQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

        secret_db_creds = secretsmanager.Secret(
            self,
            "secret_db_creds",
            secret_name="ifm/db_creds",
            description =db_name + "PostgreSQL Credentials",
            generate_secret_string=secretsmanager.SecretStringGenerator(
                secret_string_template=json.dumps({"username": "ifm"}),
                exclude_punctuation=True,
                generate_string_key="password",
            ),
        )

        # aurora_cluster_secret = secretsmanager.Secret(self, "AuroraClusterCredentials",
        #     secret_name =db_name + "AuroraClusterCredentials",
        #     description =db_name + "Aurora Cluster Credentials",
        #     generate_secret_string=secretsmanager.SecretStringGenerator(
        #         exclude_characters ="\"@/\\ '",
        #         generate_string_key ="password",
        #         password_length =30,
        #         secret_string_template='{"username":"'+aurora_cluster_username+'"}'),
        #     )  

        vpc_ifm = ec2.Vpc(
            self,
            "vpc_ifm",
            availability_zones=["eu-central-1c"],
            # max_azs=1,
            # cidr="10.5.0.0/16",
            ip_addresses=ec2.IpAddresses.cidr("10.5.0.0/16"),
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name="Public",
                    cidr_mask=26
                ),
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                    name="Private",
                    cidr_mask=26
                ),
            ],
            nat_gateways=1,
        )

        # subnet_group_ifm = rds.SubnetGroup((
        #     self,
        #     "subnet_group_ifm",
        #     vpc=vpc_ifm,
        #     vpc_subnets=ec2.SubnetSelection(
        #         subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS
        #     ),
        #     subnet_group_name="ifm-postgres-subnet-group",
        #     description="Subnet group for ifm postgres",
        # )

        security_group_ifm_db = ec2.SecurityGroup(
            self,
            "security_group_ifm_db",
            vpc=vpc_ifm,
            security_group_name="security_group_ifm_db",
            allow_all_outbound=True,
        )

        security_group_ifm_db.add_ingress_rule(
            peer=ec2.Peer.ipv4(vpc_ifm.vpc_cidr_block),
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
                version=rds.PostgresEngineVersion.VER_14
            ),
            parameters={
                "max_standby_streaming_delay": "600000",  # milliseconds (5 minutes)
                "max_standby_archive_delay": "600000",  # milliseconds (5 minutes)
            },
        )

#####################################

        # self.rds_db_postgres = rds.DatabaseInstance(
        #     self,
        #     "rds_db_postgres",
        #     instance_identifier="ifm-postgres",
        #     engine=rds.DatabaseInstanceEngine.postgres(
        #         version=rds.PostgresEngineVersion.VER_14
        #     ),
        #     instance_type=ec2.InstanceType.of(
        #         ec2.InstanceClass.M6G, ec2.InstanceSize.LARGE
        #     ),
        #     parameter_group=parameter_group_postgres,
        #     allocated_storage=200,
        #     max_allocated_storage=500,
        #     credentials=rds.Credentials.from_secret(secret_db_creds),
        #     database_name="ifmdb",
        #     vpc=vpc_ifm,
        #     # subnet_group=subnet_group_ifm,
        #     enable_performance_insights=True,
        #     performance_insight_retention=rds.PerformanceInsightRetention.DEFAULT,
        #     monitoring_interval=Duration.seconds(60),
        #     publicly_accessible=False,
        #     monitoring_role=role_enhanced_monitoring,
        #     backup_retention=Duration.days(7),
        #     security_groups=[
        #         security_group_ifm_db,
        #     ],
        # )

