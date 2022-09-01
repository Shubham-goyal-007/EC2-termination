
import boto3
from datetime import date
today = date.today()
x=today.strftime("%d-%m-%Y")
def lambda_handler(event, context ):
    AWS_REGION = "us-east-2"
    EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
    print(x)
    INSTANCE_NAME_TAG_VALUE = str(x)
    

    instances = EC2_RESOURCE.instances.filter(
    Filters=[
            {
                'Name': 'tag:delete-date',
                'Values': [
                    INSTANCE_NAME_TAG_VALUE
                ]
            }
        ]
    )

    instances.terminate()
    print(f'Instances with Tag "Name={INSTANCE_NAME_TAG_VALUE}": Is Terminated')
lambda_handler()
