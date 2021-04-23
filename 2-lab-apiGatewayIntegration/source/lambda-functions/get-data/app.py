import boto3
import os
import json
from datetime import datetime
import logging
import json

'''
AWS Lambda Function to get all data. Requests come from Amazon API Gateway.
'''

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def get_data(id):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.getenv("TABLE_NAME"))
    response = table.get_item(
        Key={
            'ID': id
        }
    )
    item = response['Item']
    return item


def handler(event, context):
    logger.info(event)
    logger.info('get-data is called')
    id = event['pathParameters']['id'] if 'id' in event['pathParameters'] else None
    if id:
        data = get_data(id)
    response =  {"statusCode": 200, "body": json.dumps({"data": data})}
    return response