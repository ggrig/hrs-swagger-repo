from aws_cdk import (core as cdk,
                     aws_ecs as ecs,
                     aws_ecr as ecr,
                     aws_logs as logs)

class APIServerBase(cdk.Construct):

    def __init__(self, scope: cdk.Construct, id:str,
                server_name:str,
                server_port:int,
                repo_arn:str,
                cluster:ecs.Cluster,
                disctinct_id: str,
                role = None,
                **kwargs):
        super().__init__(scope, id, **kwargs)

        service_prefix = server_name.lower()

        task_id = (f'{service_prefix}-td-{disctinct_id}').replace('.','-')
        log_id = f'{server_name}ServicesLogGroup'
        log_group_name = (f'/ecs/{service_prefix}-{disctinct_id}-log-group').replace('.','-')
        container_id = (f'{service_prefix}-{disctinct_id}-container').replace('.','-')
        stream_prefix = "ecs"

        task_definition = ecs.FargateTaskDefinition( self, task_id, execution_role=role, task_role=role,
                cpu=256, memory_limit_mib=512)

        repo = ecr.Repository.from_repository_arn(self, f'{service_prefix}-repo', repo_arn)

        image = ecs.ContainerImage.from_ecr_repository(repo)

        environment = {
                    "SERVER_PORT"               : server_port,
                    "SERVER_NAME"               : server_name,
                }
        
        logDetail = logs.LogGroup(self, log_id, log_group_name=log_group_name, retention=logs.RetentionDays.SIX_MONTHS, removal_policy=cdk.RemovalPolicy.DESTROY)
        logging = ecs.LogDriver.aws_logs(stream_prefix = stream_prefix, log_group=logDetail)
        container = task_definition.add_container( container_id, image=image,
                environment=environment,
                logging = logging
                )

        service = ecs.FargateService(self, id,
            task_definition=task_definition,
            assign_public_ip=True,
            cluster=cluster)