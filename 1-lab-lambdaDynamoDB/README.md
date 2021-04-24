# Lab 1: Storing and Retrieving Data from Amazon DynamoDB
In this workshop, you will build 2 AWS Lambda Functions. One AWS Lambda Function will store data, and another Lambda Function to retrieve all data from a single table in Amazon DynamoDB. This is a basic exercise to help you understand how to perform basic data storing and retrieval from Lambda functions. All of resources needed in this lab will be provisioned by AWS Cloud Development Kit (CDK). 

## Diagram
![Lab 1 Diagram](https://raw.githubusercontent.com/donnieprakoso/workshop-restAPI/main/1-lab-lambdaDynamoDB/Workshop-REST%20API-Page-1.png)

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
- You will find another 2 sub-directories named `list-data` and `store-data` 

### Step 1: Open Store Data Function
- Navigate to `work/lambda-functions/store-data`
- Open `app.py`
- Read the file thoroughly as starting from next steps, you need to work on this file.


### Step 2: Saving Data to DynamoDB
- Save data to DynamoDB with following info:
	- ID: generated random UUID string
	- date_created: datetime with format `%Y-%m-%d, %H:%M:%S`

>**💡 HINT**
>- You need to create a client to connect to AWS resources. On Python, you need to use boto3 library. 
>- Use put_item() API to save data into DynamoDB. Here's the [link](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html).

> ### 😕 Are you stuck?
> See the solution [here](https://github.com/donnieprakoso/workshop-restAPI/blob/main/1-lab-lambdaDynamoDB/source/lambda-functions/store-data/app.py)

### Step 3: Create Lambda Function to Retrieve Data
- Navigate to `work/lambda-functions/list-data`
- Open `app.py`
- Get all data from DynamoDB and make sure that you put all the results into a variable called response
- Return the Lambda function using the defined format.

>**💡 HINT**
>- Use scan() API to get all data from DynamoDB. Here's the [link](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.scan).


> ### 😕 Are you stuck?
> See the solution [here](https://github.com/donnieprakoso/workshop-restAPI/blob/main/1-lab-lambdaDynamoDB/source/lambda-functions/list-data/app.py)

### Step 4: Create an AWS CDK app
- Navigate to `work/cdk/`
- Create a file named `cdk.json`
- Open `cdk.json` and write these lines. These lines are to give a set of instruction for AWS CDK on how to build this app.
```json
{
	"app":"python3 app.py",
	"context":{}
}
```

### Step 5: Read all [TASK] on CDK app file
- Open `app.py`. In this file, you see that we are missing few things to make this as a complete code. Read the file thoroughly and go to the next steps below.

### Step 6: Define Amazon DynamoDB
- The first task on the CDK app is to create DynamoDB table. Create a CDK resource — called construct in CDK — for DynamoDB using following info:
	- id="<USE THE STACK PREFIX>-data"
    - table_name="<USE THE STACK PREFIX>-data"
    - partition_key=Use the following snippet: 
	```
	python
	_ddb.Attribute(name='ID', type=_ddb.AttributeType.STRING)
	```
    - removal_policy=core.RemovalPolicy.DESTROY (NOTE: This setting is not for production)
	- read_capacity=1
	- write_capacity=1

>**💡 HINT**
>- AWS CDK already provides a construct for DynamoDB Table. Here's the [link](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_dynamodb/Table.html).

> ### 😕 Are you stuck?
> See the solution [here](https://github.com/donnieprakoso/workshop-restAPI/blob/main/1-lab-lambdaDynamoDB/source/cdk/app.py)

### Step 7: Define IAM Permissions
- For Lambda functions able to perform activities with DynamoDB, it requires a few IAM permissions. 
- Below are the list of IAM actions needed for this workshop and it's recommended to narrow down the IAM permissions.  
	- dynamodb:PutItem
    - dynamodb:GetItem
    - dynamodb:Scan
    - dynamodb:Query
    - dynamodb:ConditionCheckItem

>**💡 HINT**
>- To specify allowed actions, you can use add_action() API on PolicyStatement. Here's the [link](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_iam/PolicyStatement.html#aws_cdk.aws_iam.PolicyStatement.add_actions).

> ### 😕 Are you stuck?
> See the solution [here](https://github.com/donnieprakoso/workshop-restAPI/blob/main/1-lab-lambdaDynamoDB/source/cdk/app.py)

### Step 8: Add DynamoDB ARN into Policy Statement
- Once that you've add all above IAM permissions, then we need to add the DynamoDB table into the policy statement
dynamodb_policy_statement.add_resources(ddb_table.table_arn)

>**💡 HINT**
>- To specify resource(s) you can use add_resources() API on PolicyStatement. Here's the [link](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_iam/PolicyStatement.html#aws_cdk.aws_iam.PolicyStatement.add_resources).

> ### 😕 Are you stuck?
> See the solution [here](https://github.com/donnieprakoso/workshop-restAPI/blob/main/1-lab-lambdaDynamoDB/source/cdk/app.py)

### Step 9: Define AWS Lambda Construct for list-data
- Create AWS Lambda Construct to list all data in DynamoDB. This is an exercise for you to define the AWS Lambda construct, and you can follow the fully working code in the store-data function. Use following info to build the construct:
	- code = Use this folder "../lambda-functions/list-data"
	- handler = "app.handler"
	- role = lambda_role
	- timeout= 60 seconds
	- runtime=Python 3.8

>**💡 HINT**
>- To create the function, you can use construct defined [here.](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_lambda/Function.html).

> ### 😕 Are you stuck?
> See the solution [here](https://github.com/donnieprakoso/workshop-restAPI/blob/main/1-lab-lambdaDynamoDB/source/cdk/app.py)


### Step 10: Add Environment Variable of DynamoDB Table for List Data function
- Add environment_variable called "TABLE_NAME" and set the value to the table name of the DynamoDB. 

>**💡 HINT**
>- Here's the [add_environment() API.](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_lambda/Function.html#aws_cdk.aws_lambda.Function.add_environment).

> ### 😕 Are you stuck?
> See the solution [here](https://github.com/donnieprakoso/workshop-restAPI/blob/main/1-lab-lambdaDynamoDB/source/cdk/app.py)

### Step 11: Tagging your AWS CDK App
- Go to the last line of `app.py` and add these following lines. It's pretty handy to keep these lines so you can tag your CDK app.
```python
core.Tags.of(stack).add('Name',stack_prefix)
app.synth()
```
### Step 11: Install all required libraries to build CDK app
- Navigate to `work/cdk/`
- Open the file named `requirements.txt`. This is a standard method to install any dependencies for Python applications. 
- Add these lines:
```
aws-cdk.core==1.96.0
aws-cdk.aws-lambda==1.96.0
aws-cdk.aws-dynamodb==1.96.0
aws-cdk.aws-iam==1.96.0
```
- Install the libraries by executing:
```bash
pip3 install -r requirements.txt
```
>**💡 HINT**
>- For more information, click on the following link to find out how to install Python requirements using pip. [Link](https://pip.pypa.io/en/stable/user_guide/#requirements-files)

### Step 12: Deploy
- Open terminal and navigate to `work/cdk/`
- Deploy the app by executing:
```bash
cdk deploy
```
### Step 13: Testing store-data Function
- Navigate to AWS Lambda Functions **store-data** [dashboard](https://ap-southeast-1.console.aws.amazon.com/lambda/home). 
- Make sure that you're in the same AWS region as you deployed your application. 
- Find the **store-data** Lambda function. To filter based on the name, you can copy and paste the function name from the CDK output or you can also filter using the stack prefix: "restAPI-lab1-lambdaDynamoDB"
- Open the link which will navigate you to the AWS Lambda Function

#### Invoking store-data Function
Now we are going to test the store data function which will save the data into Amazon DynamoDB.

- Create a test event by choosing **Test** in the upper right corner
- In the Configure test event page, choose **Create new test event** and in Event template, leave the default Hello World option. Enter an Event name and provide an empty template:
```json
{}
``` 
- Choose **Create** and then choose **Test**.

#### Let's check the record on Amazon DynamoDB
- Navigate to Amazon DynamoDB [dashboard](https://ap-southeast-1.console.aws.amazon.com/dynamodb/home?region=ap-southeast-1#tables:).
- Find the table. To filter based on the name, you can copy and paste the table name from the CDK output or you can also filter using the stack prefix: "restAPI-lab1-lambdaDynamoDB"
- If you see there's a record with data from the store-data function, then your Lambda function successfully performed activities with DynamoDB.

![Testing store-data Function](https://raw.githubusercontent.com/donnieprakoso/workshop-restAPI/main/1-lab-lambdaDynamoDB/lab1-test-dynamodb.png)

### Step 14: Testing list-data Function
- Navigate to AWS Lambda Functions **store-data** [dashboard](https://ap-southeast-1.console.aws.amazon.com/lambda/home). 
- Make sure that you're in the same AWS region as you deployed your application. 
- Find the **list-data** Lambda function. To filter based on the name, you can copy and paste the function name from the CDK output or you can also filter using the stack prefix: "restAPI-lab1-lambdaDynamoDB"
- Open the link which will navigate you to the AWS Lambda Function

#### Invoking list-data Function
Now we are going to test the store data function which will save the data into Amazon DynamoDB.

- Create a test event by choosing **Test** in the upper right corner
- In the Configure test event page, choose **Create new test event** and in Event template, leave the default Hello World option. Enter an Event name and provide an empty template:
```json
{}
``` 
- Choose **Create** and then choose **Test**.
- If you see the execution results similar to the image below, then your Lambda function successfully retrieved all data from DynamoDB

![Testing list-data Function](https://raw.githubusercontent.com/donnieprakoso/workshop-restAPI/main/1-lab-lambdaDynamoDB/lab1-test-dynamodb-list.png)

# 🤘🏻Congrats! 
You've just finished the Lab 1.

## Cleaning Up
To clean up all resources, follow these instructions below:
1. Go to `work/cdk/`
2. Run `cdk destroy` command
```bash
cdk destroy
```

