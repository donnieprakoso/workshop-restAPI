import boto3
import os
import json
from datetime import datetime
import logging
import json
import uuid

'''
AWS Lambda Function to store data. Requests come from Amazon API Gateway.
'''

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def save_to_db(data):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.getenv("TABLE_NAME"))
    response = table.update_item(
        Key={'ID': data['ID']},
        UpdateExpression="set last_updated=:sts, text_data=:text_data",
        ExpressionAttributeValues={
            ':sts': datetime.now().strftime("%m-%d-%Y %H:%M:%S"),
            ':text_data': data['text']
        })


def handler(event, context):
    logger.info(event)
    logger.info('store-data is called')
    data = json.loads(event['body'])
    data['ID'] = str(uuid.uuid4()) if "ID" not in data else data['ID']
    save_to_db(data)
    response =  {"statusCode": 200, "body": json.dumps({"message": "success"})}
    return response