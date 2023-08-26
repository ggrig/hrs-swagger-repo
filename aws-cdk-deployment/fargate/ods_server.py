import os

from aws_cdk import (core as cdk,
                     aws_ecs as ecs)

from fargate.api_server_base import APIServerBase

SERVER_NAME         = 'ODS_MOCK'
SERVER_PORT         = '8000'
REPO_ARN            = "arn:aws:ecr:eu-central-1:431647458188:repository/ods_mock"

class ODSServerConstruct(APIServerBase):

    def __init__(self, scope: cdk.Construct, id: str, cluster: ecs.Cluster, disctinct_id:str, role=None, **kwargs):
        super().__init__(scope = scope, id = id, 
            server_name = SERVER_NAME, 
            server_port = SERVER_PORT, 
            repo_arn = REPO_ARN, 
            cluster = cluster, 
            disctinct_id = disctinct_id, 
            role=role, 
            **kwargs)
