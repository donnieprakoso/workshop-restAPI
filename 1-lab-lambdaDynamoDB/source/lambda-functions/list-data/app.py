import boto3
import os
import json

DDB_TABLE = os.getenv("TABLE_NAME")


def list_data():
    data = []
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(DDB_TABLE)
    scan_kwargs = {}

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
    print("Starting Lambda function to add a record into DynamoDB")
    data = list_data()
    print("Random record added to DynamoDB Table")
    return {"statusCode": 200, "body": json.dumps({"data": data})}
