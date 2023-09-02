#!/usr/bin/env python3
import os

import aws_cdk as cdk

from postgre_sql.postgre_sql_stack import PostgreSqlStack
from dotenv import load_dotenv

load_dotenv(override=True)

aws_account_num = os.getenv ("AWS_ACCOUNT_NUM" , "")
aws_region = os.getenv ("AWS_REGION" , "")

app = cdk.App()
PostgreSqlStack(app, "PostgreSqlStack",
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    env=cdk.Environment(account=aws_account_num, region=aws_region),

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )

app.synth()
