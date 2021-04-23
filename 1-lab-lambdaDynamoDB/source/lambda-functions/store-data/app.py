import boto3
import uuid
import os
import datetime
import json

DDB_TABLE = os.getenv("TABLE_NAME")


def save_to_db(data):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(DDB_TABLE)
    table.put_item(Item=data)


def handler(event, context):
    print("Starting Lambda function to add a record into DynamoDB")
    random_string = str(uuid.uuid4())
    save_to_db({
        "ID":random_string,
        "date_created":
        datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
    })
    print("Random record added to DynamoDB Table")
    return {"statusCode": 200, "body": json.dumps({"message": "success"})}
