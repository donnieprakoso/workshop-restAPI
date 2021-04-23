import boto3
import os
import json
from datetime import datetime
import logging
import json

'''
AWS Lambda Function to delete data. Requests come from Amazon API Gateway.
'''

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def delete_from_db(id):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.getenv("TABLE_NAME"))
    table.delete_item(
        Key={
            'ID': id       
        }
    )    


def handler(event, context):    
    logger.info(event)
    logger.info('delete-data is called')
    id = event['pathParameters']['id'] if 'id' in event['pathParameters'] else None
    if id:
        delete_from_db(id)
        response =  {"statusCode": 200, "body": json.dumps({"message": "success"})}
    return response