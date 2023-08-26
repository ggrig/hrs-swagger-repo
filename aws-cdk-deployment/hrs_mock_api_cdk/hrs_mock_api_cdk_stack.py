# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
import os

from aws_cdk import (core as cdk,
                     aws_s3 as s3,
                     aws_ec2 as ec2,
                     aws_ecs as ecs,
                     aws_lambda as _lambda,
                     aws_iam as iam,
                     )

from fargate.ods_server    import ODSServerConstruct

class HRSMockAPIStack(cdk.Stack):

    def ODSServerDelpoyment(self, vpc, cluster, role=None):
        # Binance @aggTrade

        ods_server = ODSServerConstruct(self, 
                                    id = "ods_mock_server",
                                    cluster=cluster,
                                    disctinct_id="001",
                                    role=role
                                )

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, "APIServersVpc", max_azs=3)

        cluster = ecs.Cluster(self, "APIServersCluster", vpc=vpc)

        # Create a Role for ESC tasks
        ecs_tasks_role = iam.Role(self,
            id='ecs-s3-access-role',
            assumed_by=iam.ServicePrincipal("ecs-tasks.amazonaws.com"))

        self.ODSServerDelpoyment  (vpc=vpc, cluster=cluster, role=ecs_tasks_role)


        # task_switcher_lambda = _lambda.Function(
        #     self, 'TaskSwitcher',
        #     runtime=_lambda.Runtime.PYTHON_3_7,
        #     code=_lambda.Code.from_asset('lambda'),
        #     handler='task_switcher.handler',
        # )