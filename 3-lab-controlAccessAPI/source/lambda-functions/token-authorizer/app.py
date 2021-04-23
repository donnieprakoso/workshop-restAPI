import json
import jwt

def verify_token(token):
    try:
        JWT_SECRET = 'pssstttitsasecret'
        JWT_ALGORITHM = 'HS256'
        data = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
        return data
    except: 
        return None

def generate_policy(principal_ID, effect, resource):
    auth_response = {};

    auth_response['principalId'] = principal_ID;
    if effect and resource:
        policy_document = {}
        policy_document['Version'] = '2012-10-17'
        policy_document['Statement'] = []
        policy_statement = {}
        policy_statement['Action'] = 'execute-api:Invoke'
        policy_statement['Effect'] = effect
        policy_statement['Resource'] = resource
        policy_document['Statement']= [policy_statement]
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

