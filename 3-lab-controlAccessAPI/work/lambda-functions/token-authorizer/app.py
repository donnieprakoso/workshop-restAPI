import json
import jwt

def verify_token(token):
    try:
        JWT_SECRET = 'pssstttitsasecret'
        JWT_ALGORITHM = 'HS256'
        '''
        [TASK] Verify JWT token
        '''
        '''
        [END of TASK]
        '''
        return data
    except: 
        return None



def generate_policy(principal_ID, effect, resource):
    auth_response = {};

    auth_response['principalId'] = principal_ID;
    if effect and resource:
        '''
        [TASK] Define a policy document and add a policy statement
        '''        
        '''
        {
        "principalId": "<use the user_id from the decoded JWT token>", 
        "policyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": "<use the effect parameter>",
                    "Resource": "<use the resource parameter>"
                }
                ]
            },
        "context": {}
        }
        '''
        '''
        [END of TASK]
        '''        
        auth_response['policyDocument'] = policy_document

    auth_response['context'] = {}
    return auth_response


def handler(event, context):
    token = event['authorizationToken'] if 'authorizationToken' in event else None
    if token:
        data = verify_token(token)
        if data:
            auth_response = generate_policy(data['user_id'], 'Allow', event['methodArn'])
            return auth_response
        else:
            auth_response = generate_policy('', 'Deny', event['methodArn'])
            return auth_response

