#!/usr/bin/env python3

from aws_cdk import aws_iam as _iam
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_dynamodb as _ddb
from aws_cdk import aws_apigateway as _ag
from aws_cdk import core


class CdkStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, stack_prefix: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

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

        # AWS Lambda Functions
        fnLambda_secureAPI = _lambda.Function(
            self,
            "{}-function-secureApi".format(stack_prefix),
            code=_lambda.AssetCode("../lambda-functions/secure-api"),
            handler="app.handler",
            timeout=core.Duration.seconds(60),
            role=lambda_role,
            runtime=_lambda.Runtime.PYTHON_3_8)

        fnLambda_authorizer = _lambda.Function(
            self,
            "{}-function-tokenAuthorizer".format(stack_prefix),
            code=_lambda.AssetCode("../lambda-functions/token-authorizer"),
            handler="app.handler",
            timeout=core.Duration.seconds(60),
            role=lambda_role,
            runtime=_lambda.Runtime.PYTHON_3_8)

        api = _ag.RestApi(
            self,
            id="{}-api-gateway".format(stack_prefix),
        )

        api_authorizer = _ag.TokenAuthorizer(self, id="{}-authorizer".format(stack_prefix),
        handler=fnLambda_authorizer)

        int_secure_api = _ag.LambdaIntegration(fnLambda_secureAPI)

        res_data = api.root.add_resource('api')
        res_data.add_method('GET',int_secure_api, authorizer = api_authorizer)

        core.CfnOutput(self, "{}-output-apiEndpointURL".format(stack_prefix),
                       value=api.url, export_name="{}-apiEndpointURL".format(stack_prefix))


stack_prefix = 'restAPI-lab3-secureAPI'
app = core.App()
stack = CdkStack(app, stack_prefix, stack_prefix=stack_prefix)
core.Tags.of(stack).add('Name', stack_prefix)

app.synth()
