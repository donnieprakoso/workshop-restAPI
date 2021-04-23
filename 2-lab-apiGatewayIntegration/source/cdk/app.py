#!/usr/bin/env python3

from aws_cdk import aws_iam as _iam
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_dynamodb as _ddb
from aws_cdk import aws_apigateway as _ag
from aws_cdk import core


class CdkStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, stack_prefix: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Model all required resources
        ddb_table = _ddb.Table(
            self,
            id='{}-data'.format(stack_prefix),
            table_name='{}-data'.format(stack_prefix),
            partition_key=_ddb.Attribute(name='ID',
                                         type=_ddb.AttributeType.STRING),
            removal_policy=core.RemovalPolicy.DESTROY,# THIS IS NOT RECOMMENDED FOR PRODUCTION USE
            read_capacity=1,
            write_capacity=1)

        # IAM Roles
        lambda_role = _iam.Role(
            self,
            id='{}-lambda-role'.format(stack_prefix),
            assumed_by=_iam.ServicePrincipal('lambda.amazonaws.com'))

        cw_policy_statement = _iam.PolicyStatement(effect=_iam.Effect.ALLOW)
        cw_policy_statement.add_actions("logs:CreateLogGroup")
        cw_policy_statement.add_actions("logs:CreateLogStream")
        cw_policy_statement.add_actions("logs:PutLogEvents")
        cw_policy_statement.add_actions("logs:DescribeLogStreams")
        cw_policy_statement.add_resources("*")
        lambda_role.add_to_policy(cw_policy_statement)

        # Add role for DynamoDB
        dynamodb_policy_statement = _iam.PolicyStatement(
            effect=_iam.Effect.ALLOW)
        dynamodb_policy_statement.add_actions("dynamodb:PutItem")
        dynamodb_policy_statement.add_actions("dynamodb:GetItem")
        dynamodb_policy_statement.add_actions("dynamodb:UpdateItem")
        dynamodb_policy_statement.add_actions("dynamodb:DeleteItem")
        dynamodb_policy_statement.add_actions("dynamodb:Scan")
        dynamodb_policy_statement.add_actions("dynamodb:Query")
        dynamodb_policy_statement.add_actions("dynamodb:ConditionCheckItem")
        dynamodb_policy_statement.add_resources(ddb_table.table_arn)
        lambda_role.add_to_policy(dynamodb_policy_statement)

        # AWS Lambda Functions
        fnLambda_saveData = _lambda.Function(
            self,
            "{}-function-saveData".format(stack_prefix),
            code=_lambda.AssetCode("../lambda-functions/save-data"),
            handler="app.handler",
            timeout=core.Duration.seconds(60),
            role=lambda_role,
            runtime=_lambda.Runtime.PYTHON_3_8)
        fnLambda_saveData.add_environment("TABLE_NAME", ddb_table.table_name)

        fnLambda_listData = _lambda.Function(
            self,
            "{}-function-listData".format(stack_prefix),
            code=_lambda.AssetCode("../lambda-functions/list-data"),
            handler="app.handler",
            timeout=core.Duration.seconds(60),
            role=lambda_role,
            runtime=_lambda.Runtime.PYTHON_3_8)
        fnLambda_listData.add_environment("TABLE_NAME", ddb_table.table_name)

        fnLambda_getData = _lambda.Function(
            self,
            "{}-function-getData".format(stack_prefix),
            code=_lambda.AssetCode("../lambda-functions/get-data"),
            handler="app.handler",
            timeout=core.Duration.seconds(60),
            role=lambda_role,
            runtime=_lambda.Runtime.PYTHON_3_8)
        fnLambda_getData.add_environment("TABLE_NAME", ddb_table.table_name)

        fnLambda_deleteData = _lambda.Function(
            self,
            "{}-function-deleteData".format(stack_prefix),
            code=_lambda.AssetCode("../lambda-functions/delete-data"),
            handler="app.handler",
            timeout=core.Duration.seconds(60),
            role=lambda_role,
            runtime=_lambda.Runtime.PYTHON_3_8)
        fnLambda_deleteData.add_environment("TABLE_NAME", ddb_table.table_name)

        api = _ag.RestApi(
            self,
            id="{}-api-gateway".format(stack_prefix),
        )

        int_saveData = _ag.LambdaIntegration(fnLambda_saveData)
        int_listData = _ag.LambdaIntegration(fnLambda_listData)
        int_getData = _ag.LambdaIntegration(fnLambda_getData)
        int_deleteData = _ag.LambdaIntegration(fnLambda_deleteData)
        
        res_data = api.root.add_resource('data')
        res_data.add_method('POST',int_saveData)
        res_data.add_method('GET',int_listData)

        res_data_id = res_data.add_resource('{id}')
        res_data_id.add_method('GET',int_getData)
        res_data_id.add_method('DELETE',int_deleteData)

        core.CfnOutput(self, "{}-output-dynamodbTable".format(stack_prefix),
                       value=ddb_table.table_name, export_name="{}-ddbTable".format(stack_prefix))
        core.CfnOutput(self, "{}-output-apiEndpointURL".format(stack_prefix),
                       value=api.url, export_name="{}-apiEndpointURL".format(stack_prefix))


stack_prefix = 'restAPI-lab2-apiGatewayIntegration'
app = core.App()
stack = CdkStack(app, stack_prefix, stack_prefix=stack_prefix)
core.Tags.of(stack).add('Name', stack_prefix)

app.synth()
