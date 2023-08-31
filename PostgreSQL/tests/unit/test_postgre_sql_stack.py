import aws_cdk as core
import aws_cdk.assertions as assertions

from postgre_sql.postgre_sql_stack import PostgreSqlStack

# example tests. To run these tests, uncomment this file along with the example
# resource in postgre_sql/postgre_sql_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = PostgreSqlStack(app, "postgre-sql")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
