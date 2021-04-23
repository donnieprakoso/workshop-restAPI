import boto3
import os
import json
from datetime import datetime
import logging
import json

'''
AWS Lambda Function to list all data. Requests come from Amazon API Gateway.
'''

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def list_data():
    data = []
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.getenv("TABLE_NAME"))
    scan_kwargs = {}
    scan_kwargs["ProjectionExpression"]="ID"

    done = False
    start_key = None
    while not done:
        if start_key:
            scan_kwargs['ExclusiveStartKey'] = start_key
        response = table.scan(**scan_kwargs)
        data.extend(response.get('Items'))
        start_key = response.get('LastEvaluatedKey', None)
        done = start_key is None
    return data


def handler(event, context):
    logger.info(event)
    logger.info('list-data is called')
    data = list_data()    
    response =  {"statusCode": 200, "body": json.dumps({"data": data})}
    return response