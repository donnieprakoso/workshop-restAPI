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
        '''
        [TASK] Get all data by using scan API and pass scan_kwargs as parameter and name the variable as 'response'
        All results from DynamoDB will be stored in 'Items' and you need to extend (not append) the data variable to include the 'Items'
        '''
        '''
        [END OF TASK] 
        '''        
        start_key = response.get('LastEvaluatedKey', None)
        done = start_key is None
    return data


def handler(event, context):
    print("Starting Lambda function to add a record into DynamoDB")
    data = list_data()
    print("Random record added to DynamoDB Table")
    '''
    [TASK] Return the response in dictionary with following format:
    {
        statusCode: 200
        body:
        {
            data: data
        }
    }
    Please note that the body need to be dumped in JSON format
    '''

    '''
    [END OF TASK]
    '''    
