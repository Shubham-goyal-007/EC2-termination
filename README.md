# EC2-termination
 Automate Termination of EC2 Instances base on Tags using Lambda function and EventBridge(CloudWatch Events)
 
#Prerequisite 
An AWS account

Install awscli using aws official documentation here 

Install python and boto3 

Configure aws cli by using official documentation here 

#Boto3 
Boto3 is the name of the Python SDK for AWS. It allows you to directly create, update, and delete AWS resources from your Python scripts. 

#Steps to automate termination of EC2 instance having tag: 
Launch EC2 instance having a tag with key value. 

Create IAM role->create policy->use EC2 as service->In action choose Terminate Instance and add another policy name” AmazonEC2ReadOnlyAccess” 

Create a lambda function (Author from scratch) choose existing role which were create in IAM policy. 

Deploy your python code and test the code. 

Create Cloud Watch Events->Create Rule->In Event Source->Choose scheduler in which add Cronjob which runs on every day at 2pm. 

In target choose lambda function which is created earlier. 
