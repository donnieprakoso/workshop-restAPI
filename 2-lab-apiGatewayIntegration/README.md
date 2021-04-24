# Lab 2: Implementing REST API with Amazon API Gateway
This lab is the main content of this workshop where you are going to implement REST API with Amazon API Gateway, AWS Lambda and Amazon DynamoDB. You will learn how to build resources following REST API guidelines using HTTP protocol and methods. 

You will build 4 AWS Lambda Functions, each of them are integrated with Amazon API Gateway endpoint and respective HTTP method. There are few small details in this lab that you'll find useful while building your API, for examples: defining resources and how to get URL parameters. 

## Diagram
![Lab 2 Diagram](https://raw.githubusercontent.com/donnieprakoso/workshop-restAPI/main/2-lab-apiGatewayIntegration/Workshop-REST%20API-Page-2.png)

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

### Step 1: Structuring AWS Lambda Functions work folders
- Navigate to `work/lambda-functions/` folder
- You will find 5 sub-directories in this folder: 
1. `save-data`
2. `list-data`
3. `get-data`
4. `delete-data`

### Step 2: Working on `save-data`
- Navigate to `work/lambda-functions/save-data`
- Open `app.py`

### Step 3: Get request payload 
- Get the request payload from `event` variable and use `data` as name of the variable. 

>**💡 HINT**
- Amazon API Gateway invokes your function synchronously with an event. This event contains JSON representation of the HTTP request. You can refer to following link, to see the example of the structure. [Link](https://github.com/awsdocs/aws-lambda-developer-guide/blob/main/sample-apps/nodejs-apig/event.json)
- Request payload is stored in `body`
- As the request payload in `event` is in JSON format, you'll need to load the JSON string. [Link](https://docs.python.org/3/library/json.html#json.loads)

> ### 😕 Are you stuck?
> See the solution [here](https://github.com/donnieprakoso/workshop-restAPI/blob/main/2-lab-apiGatewayIntegration/source/lambda-functions/save-data/app.py)

### Step 4: Working on `list-data`
- Navigate to `work/lambda-functions/list-data`
- Open `app.py`

### Step 5: Specify the attributes
- One way to list all data, you will need to use `scan` API. In this case, you need to specify to return only field "ID" to reduce the size of response returned to client. 

>**💡 HINT**
- Use `ProjectionExpression` parameter to return only specific attributes. [Link](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.scan)

> ### 😕 Are you stuck?
> See the solution [here](https://github.com/donnieprakoso/workshop-restAPI/blob/main/2-lab-apiGatewayIntegration/source/lambda-functions/list-data/app.py)

### Step 6: Working on `get-data`
- Navigate to `work/lambda-functions/get-data`
- Open `app.py`

### Step 7: Get specific record from DynamoDB
- In the `get_data` function, you need to get a record based on its ID. Use the `id` parameter in your DynamoDB call.

>**💡 HINT**
- Use `get_item()` API to return an item with the given primary key. [Link](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.get_item)

> ### 😕 Are you stuck?
> See the solution [here](https://github.com/donnieprakoso/workshop-restAPI/blob/main/2-lab-apiGatewayIntegration/source/lambda-functions/get-data/app.py)

### Step 8: Load path parameters from `event` variable
- To get the ID from the request, you need to load the path parameters of the request. Use `id` as the variable name.

>**💡 HINT**
- Similar to the request payload, all path parameters are also stored in the `event`. Refer to the following link to figure out which variables holds the `pathParameters` . [Link](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.get_item)

> ### 😕 Are you stuck?
> See the solution [here](https://github.com/donnieprakoso/workshop-restAPI/blob/main/2-lab-apiGatewayIntegration/source/lambda-functions/get-data/app.py)

### Step 9: Working on `delete-data`
**You don't need to do anything.** This is already been provided in the `work/lambda-functions/delete-data/app.py` file as a complete code.

### Step 10: Setting cdk.json
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

### Step 12: Create REST API Object
- Before you can integrate Lambda functions and Amazon API Gateway, you need to create a REST API object. 

>**💡 HINT**
>- Use `RestApi` construct. Here's the [API reference](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_apigateway/RestApi.html#restapi).

> ### 😕 Are you stuck?
> See the solution [here](https://github.com/donnieprakoso/workshop-restAPI/blob/main/2-lab-apiGatewayIntegration/source/cdk/app.py)

### Step 13: Create integrations for each Lambda Functions
- To integrate Lambda functions and Amazon API Gateway, you'll need to create integration using `LambdaIntegration` for each Lambda functions. 
- By the end of this task, you should have 4 `LambdaIntegration` objects.
        
      
>**💡 HINT**
>- Here's the [API reference](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_apigateway/LambdaIntegration.html).

> ### 😕 Are you stuck?
> See the solution [here](https://github.com/donnieprakoso/workshop-restAPI/blob/main/2-lab-apiGatewayIntegration/source/cdk/app.py)

### Step 14: Create REST resource
- At this point, you have a `RestApi` object and 4 `LambdaIntegration` objects. Now you need to create a REST resource. 
- There are two resources that you need to create: `data` and `data/item_id`. The example of endpoint for our API is as follow: `http://example.com/data` and `http://example.com/data/item_id`
- For this task, you need to create `data` resource.

>**💡 HINT**
>- To add resources for your `RestApi` object, you need to access the `root` as it represents the root resource (`/`) of your API endpoint.
>- Here's the reference to `root` base. [Link](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_apigateway/RestApiBase.html#aws_cdk.aws_apigateway.RestApiBase.root)
>- ...which will lead you to `IResource` class where you can do operations. [Link](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_apigateway/IResource.html#aws_cdk.aws_apigateway.IResource)
>- Use following API link to add resources. [Link](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_apigateway/IResource.html#aws_cdk.aws_apigateway.IResource.add_resource)

> ### 😕 Are you stuck?
> See the solution [here](https://github.com/donnieprakoso/workshop-restAPI/blob/main/2-lab-apiGatewayIntegration/source/cdk/app.py)
 
### Step 14: Create HTTP methods for `/data` resource
- Once you have defined the `/data` resource, now you need to define what the HTTP methods available for this resource.
- There are 2 methods you need to define for this resource: 1) POST method for `save-data` and 2) GET method for `list-data`

>**💡 HINT**
>- Use following API link to add method. [Link](https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_apigateway/IResource.html#aws_cdk.aws_apigateway.IResource.add_method)
>- Use the Lambda integration objects that you've created earlier as the `target` parameter for `add_method()`.

> ### 😕 Are you stuck?
> See the solution [here](https://github.com/donnieprakoso/workshop-restAPI/blob/main/2-lab-apiGatewayIntegration/source/cdk/app.py)

### Step 15: Add path parameter `id` within `data` resource
- To get data details and to delete a data, you'll need to pass the ID. This is the endpoint example: `http://example.com/data/96bbcaff-6546-4e85-b246-9f61fa94c173`. 
- To assign a path parameter, use `{VARIABLE_NAME}` while calling `add_resource()` on the `data` resource object.

> ### 😕 Are you stuck?
> See the solution [here](https://github.com/donnieprakoso/workshop-restAPI/blob/main/2-lab-apiGatewayIntegration/source/cdk/app.py)

### Step 16: Create HTTP methods for `/data` resource
- There are 2 methods you need to define for this resource: 1) GET method for `get-data` and 2) DELETE method for `delete-data`

> ### 😕 Are you stuck?
> See the solution [here](https://github.com/donnieprakoso/workshop-restAPI/blob/main/2-lab-apiGatewayIntegration/source/cdk/app.py)

### Step 17: Install all required libraries to build and run CDK app
- Open your terminal
- Navigate to `work/cdk/`
- Create a file named `requirements.txt`. This is a standard method to install any dependencies for Python applications. 
- Add these lines:
```
aws-cdk.core==1.96.0
aws-cdk.aws-iam==1.96.0
aws-cdk.aws-lambda==1.96.0
aws-cdk.aws-apigateway==1.96.0
aws-cdk.aws-dynamodb==1.96.0
```
- Install the libraries by executing:
```bash
pip install -r requirements.txt
```
### Step 18: Deploy
- Open your terminal
- Navigate to `work/cdk/`
- Deploy the app by executing:
```bash
cdk deploy
```
- When you successfully deployed the CDK APP, you will get an API endpoint running on Amazon API Gateway. **Note down this URL.**

#### ⚠️ Time for Testing ⚠️
- Congrats! At this point, you have a REST API running on Amazon API Gateway and integrated with AWS Lambda. 
- For testing, we're going to do 4 scenarios:
    1. Add a couple of data using `save-data` API
    2. List data using `list-data` API
    3. Get a data using `get-data` API
    4. Delete a data using `delete-data` API
- There are few ways on doing this, and for you who have cURL installed, I've prepared a simple `bash` script that you can execute. 
- Before you execute the bash script, you need to change the API endpoint to your endpoint.
- If you don't have cURL installed, refer to this [page](https://curl.se/download.html) to learn how to install.

### Step 19: Add couple of data
**⚠️ Before you execute the bash script, you need to change the API endpoint to your endpoint**

- Open your terminal and navigate to `work/testing-api/`
- Run `save-data.sh` more than 1 time to add data. 
- Let's check DynamoDB table. Go to [DynamoDB dashboard](https://ap-southeast-1.console.aws.amazon.com/dynamodb/home?region=ap-southeast-1#tables:) and filter the tables with `restAPI` or you can get the name of the table from the `deploy` output.
- Open the table.
- If you see couple of records in your table, then your API works. 

### Step 20: List all data
**⚠️ Before you execute the bash script, you need to change the API endpoint to your endpoint**

- Run `list-data.sh` to get all data
- You will get response from the API all data with their IDs. 
- You won't see other fields as we set `ProjectionExpression` to only select `ID` field.
- Note one of the IDs for next step. 

### Step 21: Get details of a data
**⚠️ Before you execute the bash script, you need to change the API endpoint to your endpoint**

- Run `get-data.sh` and enter the data ID
- You'll get the full data details.

### Step 22: Delete a data
**⚠️ Before you execute the bash script, you need to change the API endpoint to your endpoint**

- Run `delete-data.sh` and enter the data ID
- Run `list-data.sh` to get all data
- Check if the data with the `ID` you specified in this step has been deleted.

# 🤘🏻Congrats! 
You've just finished the Lab 2.

## Cleaning Up
To clean up all resources, follow these instructions below:
1. Go to `work/cdk/`
2. Run `cdk destroy` command
```bash
cdk destroy
```