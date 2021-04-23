## 🚀 Workshop — Building REST APIs with AWS

In this workshop, you will build and deploy a REST API using Amazon API Gateway, AWS Lambda, and AWS CDK (and a bit of Amazon DynamoDB).
The main objective of this workshop is to build a foundation of understanding how to implement REST API with AWS and also how to adopt IaC for reusable APIs.

The content of this workshop will be updated regularly and if you have questions or find issues in this workshop, please file them as an Issue.

## Workshop Structure
Each lab in this workshop can be run separately. Each labs consist of full working source code along with AWS CDK to easily provision and destroy created resources.

#### Lab 1: Integrating AWS Lambda with Amazon DynamoDB
The objective of this lab is to help you understand how to develop AWS Lambda to perform some activities with Amazon DynamoDB. This is considered as a good exercise — as you develop APIs with AWS serverless services — you will encounter many use-cases that requires integration between AWS Lambda and Amazon DynamoDB. 

In this workshop, you will build 2 AWS Lambda Functions. One AWS Lambda Function will store data, and another Lambda Function to retrieve all data from a single table in Amazon DynamoDB. This is a basic exercise to help you understand how to perform basic data storing and retrieval from Lambda functions. All of resources needed in this lab will be provisioned by AWS Cloud Development Kit (CDK). 

[💻 Start This Lab](https://github.com/donnieprakoso/workshop-restAPI/tree/main/1-lab-lambdaDynamoDB)

#### Lab 2: Implementing REST API with Amazon API Gateway
This lab is the main content of this workshop where you are going to implement REST API with Amazon API Gateway, AWS Lambda and Amazon DynamoDB. You will learn how to build resources following REST API guidelines using HTTP protocol and methods. 

You will build 4 AWS Lambda Functions, each of them are integrated with Amazon API Gateway endpoint and respective HTTP method. There are few small details in this lab that you'll find useful while building your API, for examples: defining resources and how to get URL parameters. 

[💻 Start This Lab](https://github.com/donnieprakoso/workshop-restAPI/tree/main/2-lab-apiGatewayIntegration)

#### Lab 3: Controlling Access with Lambda Authorizer

In this lab, you will build a basic API that needs to be secured by Lambda Authorizer using token. The token takes form of JWT. Please be noted that in this lab we will not cover authentication and authorizatio platform. 
 
You will learn how to use Lambda Authorizer and how to integrate with Amazon API Gateway using AWS CDK, to control the access of your API. 

[💻 Start This Lab](https://github.com/donnieprakoso/workshop-restAPI/tree/main/3-lab-controlAccessAPI)

---
## Workshop Level
This workshop welcomes developers of all levels. 

This workshop is structured as puzzles in which you need to complete a set of partial codes into a complete code. It is an intended design to help build an understanding of a specific concept. Also, to help you get familiar with common resources needed to develop with AWS services.

---
## 🛑 First Thing First
If this is your first time using this workshop, this section is an important piece that you need to read before moving on.

⚠️
>  Please make sure that your development environment meets the requirements below and properly configured before starting any of the workshops.

**Workshop Requirements**

Requirement | More Information | Notes  
---|---|---   
Active AWS Account | [Link](https://aws.amazon.com/) |  Mandatory requirement   
AWS CDK | [Link](https://aws.amazon.com/cdk/) |Require Node JS   
AWS CLI | [Link](https://aws.amazon.com/cli/) |Require active    AWS account. Please configure your account as described on this    [page](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) 
Python 3.8 | [Link](https://www.python.org/downloads/release/python-380/) |Most of the workshop will be using Python 3.8   
Boto3 | [Link](https://aws.amazon.com/sdk-for-python/) | Amazon Web Services (AWS) Software Development Kit (SDK) for Python
Node JS 10.30 or later | [Link](https://nodejs.org/en/download/current/) |Node.js versions 13.0.0 through 13.6.0 are not compatible with the AWS CDK


⚠️
> Since we will be using AWS CDK extensively in this workshop, please properly configure AWS CDK for your development environment. 

**If you haven't done that, please follow the instruction [here](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html).**

In summary, here's a quick checklist to complete the required checking.  
- [ ] Installed AWS CLI  
- [ ] Configured AWS CLI with `aws configure`  
- [ ] Installed Node JS  
- [ ] Installed AWS CDK with `npm install -g aws-cdk`  
- [ ] Configured AWS CDK with `cdk bootstrap`  

### **💡 HINT** and 😕 Are you stuck? 
For the more complex tasks that you need to complete, there will be a **💡 HINT** to guide you on how to solve it. Most of the time, it will also include link(s) for further reading. 

Please remember that if you are stuck and can't move to the next step, you can always see the main reference file to see the solution. For easy access, **😕 Are you stuck?** will guide you directly to the solution.

## AWS Services
Some of the services from AWS that are used in this workshop are as follows:  
- [AWS CDK](https://aws.amazon.com/cdk/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon API Gateway](https://aws.amazon.com/api-gateway/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)

## ⚠️  Cleaning Up
This workshop uses AWS services that are mostly covered by the Free Tier allowance - ONLY if your account is less than 12 months old. For accounts passed the free tier eligibility, it may incur some costs. To minimize the cost, make sure you **delete resources used in this workshop when you are finished**.

All of the labs in this workshop use a standardized cleaning method with AWS CDK.
1. Go to each lab
2. Change the directory to `cdk /`
3. Run `cdk destroy`
4. If in some cases it fails, you need to go to [AWS CloudFormation](https://console.aws.amazon.com/cloudformation/) to manually delete the stack.

