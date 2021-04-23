import boto3
import uuid
import os
import datetime
import json

DDB_TABLE = os.getenv("TABLE_NAME")


def save_to_db(data):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(DDB_TABLE)
    '''
    [TASK] Save the data into database ONLY by using put_item API
    '''

    '''
    [END OF TASK]
    '''

def handler(event, context):
    print("Starting Lambda function to add a record into DynamoDB")
    random_string = str(uuid.uuid4())
    save_to_db({
        "ID":random_string,
        "date_created":
        datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
    })
    print("Random record added to DynamoDB Table")
    
    '''
    [TASK] Return the response in dictionary with following format:
    {
        statusCode: 200
        body:
        {
            message: success
        }
    }
    Please note that the body need to be dumped in JSON format
    '''

    '''
    [END OF TASK]
    '''
