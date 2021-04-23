#!/usr/bin/env python3

from aws_cdk import aws_iam as _iam
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_dynamodb as _ddb
from aws_cdk import core


class CdkStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, stack_prefix:str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create DynamoDB Table
        '''
        [TASK] Create DynamoDB Table. Use this variable name: ddb_table
        '''

        '''
        [END of TASK]
        '''
        
        ## Define IAM Roles
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
        '''
        [TASK] Define IAM Roles for Lambda to do activities with DynamoDB
        '''
        '''
        [END of TASK]
        '''
        '''
        [TASK] Add DynamoDB Table ARN resource into the policy statement
        '''
        '''
        [END of TASK]
        '''


        lambda_role.add_to_policy(dynamodb_policy_statement)
        
        ## AWS Lambda Functions
        fnLambda_storeData = _lambda.Function(
            self, 
            "{}-function-storeData".format(stack_prefix),
            code=_lambda.AssetCode("../lambda-functions/store-data"),
            handler="app.handler",
            timeout=core.Duration.seconds(60),
            role=lambda_role,
            runtime=_lambda.Runtime.PYTHON_3_8)
        fnLambda_storeData.add_environment("TABLE_NAME", ddb_table.table_name)

        '''
        [TASK] Define AWS Lambda Function for list-data. Use this variable name: fnLambda_listData
        '''
        
        '''
        [END of TASK] 
        '''

        '''
        [TASK] Add environment_variable for DynamoDB Table name so AWS Lambda Function can use the variable
        '''
        
        '''
        [END of TASK] 
        '''        
        

        core.CfnOutput(self, "{}-output-dynamodbTable".format(stack_prefix), value=ddb_table.table_name, export_name="{}-ddbTable".format(stack_prefix))
        core.CfnOutput(self, "{}-output-lambdaStoreData".format(stack_prefix), value=fnLambda_storeData.function_name, export_name="{}-lambdaStoreDataName".format(stack_prefix))
        core.CfnOutput(self, "{}-output-lambdaListData".format(stack_prefix), value=fnLambda_listData.function_name, export_name="{}-lambdaListDataName".format(stack_prefix))

stack_prefix='restAPI-lab1-lambdaDynamoDB'
app = core.App()
stack = CdkStack(app, stack_prefix, stack_prefix=stack_prefix)
'''
[TASK] Tag CDK App
'''
'''
[END of TASK]
'''
