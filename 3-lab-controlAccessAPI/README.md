# Lab 3: Defining Access Control for REST API Using Lambda Authorizer
A Lambda authorizer uses a Lambda function to control access to API in Amazon API Gateway. This particular feature is useful if you want to implement a custom authorization scheme that uses a bearer token authorization strategy.

There are two types of Lambda authorizers, 1) Token Authorizer and 2) Request Authorizer. Token Authorizer uses bearer token in form of JWT or OAuth token and the Request Authorizer uses combination of headers, query string parameters, stageVariables, and $context variables.

In this lab, you will build a basic API that needs to be secured by Lambda Authorizer using token. The token takes form of JWT. Please be noted that in this lab we will not cover authentication and authorization platform. 
 
You will learn how to use Lambda Authorizer and how to integrate with Amazon API Gateway using AWS CDK, to control the access of your API. 

## Diagram
![Lab 3 Diagram](https://github.com/donnieprakoso/workshop-restAPI/blob/main/3-lab-controlAccessAPI/lab3-diagram.png)

## Tasks
These are the tasks that you need to complete. If at some point you are stuck, please refer to the primary reference located at `source/` folder. 

### Step 0: Prepare work folder and boto3
#### Install boto3 library
- Open your terminal
- Run this command
```bash
pip install boto3 
```

#### Preparing work folder
- Navigate to `work/` folder
- You will find 2 sub-directories named `cdk` and `lambda-functions`
- Navigate to `work/lambda-functions/` 
- You will find 3 sub-directories of AWS Lambda Functions. 

### Step 1: Working on `secure-api` Lambda Function
**You don't need to do anything.** This is already been provided in the `work/lambda-functions/secure-api/app.py` file as a complete code.

### Step 2: Working on `token-authorizer` Lambda Function
- Navigate to `work/lambda-functions/token-authorizer/`
- Open `app.py`

### Step 3: Verify JWT Token
- In `verify-token` function, you need to complete the code by decoding the JWT token and verifying using the provided secret and algorithm. 
- Use `data` as the variable name for the decoded JWT token

> **💡 HINT**   
> - This lab uses PyJWT library. Here's the link to see how to decode the token. [Link](https://pyjwt.readthedocs.io/en/latest/usage.html#encoding-decoding-tokens-with-hs256)

> ### 😕 Are you stuck?
> See the solution [here](https://github.com/donnieprakoso/workshop-restAPI/blob/main/3-lab-controlAccessAPI/source/lambda-functions/token-authorizer/app.py)

### Step 4: Define a policy document and policy statement
- Your Lambda authorizer, needs to return output in a dictionary object so API Gateway knows if the request is allowed or denied. 
- To make it easier for you defining the object, you can follow the JSON object defined in the working file.

> **💡 HINT**   
> - To see the complete reference and details, click on this [link](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-lambda-authorizer-output.html). 

> ### 😕 Are you stuck?
> See the solution [here](https://github.com/donnieprakoso/workshop-restAPI/blob/main/3-lab-controlAccessAPI/source/lambda-functions/token-authorizer/app.py)

### Step 5: Working on the AWS CDK App
#### Navigate to work folder
- Navigate to `work/cdk/`
- Create a file named `cdk.json`
- Open `cdk.json` and write these lines. These lines are to give a set of instruction for AWS CDK on how to build this app.
```json
{
	"app":"python3 app.py",
	"context":{}
}
```

- Open `app.py`. In this file, you see that we are missing few things to make this as a complete code. Read the file thoroughly and go to the next steps below.

### Step 6: Create TokenAuthorizer object
- Create `TokenAuthorizer` object and use the handler set the `handler` to the `authorizer` Lambda function.

> **💡 HINT**   
> - Use TokenAuthorizer construct to createthe object. Here's the [API reference](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_apigateway/TokenAuthorizer.html).

> ### 😕 Are you stuck?
> See the solution [here](https://github.com/donnieprakoso/workshop-restAPI/blob/main/3-lab-controlAccessAPI/source/cdk/app.py)

### Step 7: Adding GET method and setting the authorizer
- In above lines, you'll see that we've defined the resource using `add_resource()` and set the URL resource to `api`. This means that the request will need to go to `/api` endpoint.
- To control the access, you will need to add the authorizer when you `add_method` for your API.

> **💡 HINT**   
> - Use `authorizer` parameter to set the authorizer. Here's the [API reference](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_apigateway/IResource.html#aws_cdk.aws_apigateway.IResource.add_method).

> ### 😕 Are you stuck?
> See the solution [here](https://github.com/donnieprakoso/workshop-restAPI/blob/main/3-lab-controlAccessAPI/source/cdk/app.py)

### Step 8: Install `token-authorizer` function library
- As the `token-authorizer` uses external library, we need to install the libraries into the folder so CDK can deploy the function alongside with the libraries.
- Open your terminal
- Navigate to `work/lambda-functions/token-authorizer/`
- Open `requirements.txt`
- Check if there's `PyJWT` on the first line, if not, you'll need to add it
- Install the requirements into the folder using following command: `pip install -r requirements.txt -t .`

> **💡 HINT**   
> - If you're new to AWS Lambda, the following link will help you to understand how to package your Lambda function if you have external runtime dependencies. [Link](https://docs.aws.amazon.com/lambda/latest/dg/python-package-create.html#python-package-create-with-dependency)


### Step 9: Install all required libraries to build and run CDK app
- Open your terminal
- Navigate to `work/cdk/`
- Create a file named `requirements.txt`. This is a standard method to install any dependencies for Python applications. 
- Add these lines:
```
aws-cdk.core==1.96.0
aws-cdk.aws-iam==1.96.0 
aws-cdk.aws-lambda==1.96.0
aws-cdk.aws-apigateway==1.96.0
```

- Install the libraries by executing:
```bash
pip3 install -r requirements.txt
```

### Step 10: Deploy
- Open your terminal
- Navigate to `work/cdk/`
- Deploy the app by executing:
```bash
cdk deploy
```
- When you successfully deployed the CDK APP, you will get an API endpoint running on Amazon API Gateway. **Note down this URL.**

#### ⚠️ Time for Testing ⚠️
- For testing, we're going to do 2 scenarios:
    1. Using random string as the authorization token — which will make the requests failed
    2. Using JWT token which will led to successful request

#### ⚠️ Wait, what JWT token? ⚠️
- Use the following JWT token that I generated from [JWT.io](https://jwt.io):
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwidXNlcl9pZCI6InVzZXItdGVzdC1qd3QiLCJpYXQiOjE1MTYyMzkwMjJ9.c9BqfJp04T9E3ulM97ruVmedwhT4AWyGfL3dPCSrSr4
```
- If you remember when you were working on `token-authorizer` function, we have defined the JWT token secret. 
- You also can decode the JWT token at [JWT.io](https://jwt.io) by copy and paste the token, and also setting the secret from the Lambda function

### Step 11: Testing with random string
- Open terminal
- Execute this command:
```bash
curl -H "Authorization: THIS_IS_A_RANDOM_STRING" <https://your-api-endpoint>
```
- If you see the following response, then your authorizer works correctly
```json
{"Message":"User is not authorized to access this resource with an explicit deny"}
```

### Step 12: Testing with correct token
- Open terminal
- Execute this command:
```bash
curl -H "Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwidXNlcl9pZCI6InVzZXItdGVzdC1qd3QiLCJpYXQiOjE1MTYyMzkwMjJ9.c9BqfJp04T9E3ulM97ruVmedwhT4AWyGfL3dPCSrSr4" <https://your-api-endpoint>
```
- If you see the following response, then your authorizer works correctly. 
```json
{"message": "success"}
```
- This is the response from your `secure-api` Lambda function

# 🤘🏻Congrats! 
You've just finished the Lab 3.

## Cleaning Up
To clean up all resources, follow these instructions below:
1. Go to `work/cdk/`
2. Run `cdk destroy` command
```bash
cdk destroy
```