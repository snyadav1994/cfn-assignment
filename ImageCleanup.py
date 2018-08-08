import boto3
from botocore.exceptions import ClientError
import sys


role_arn = "arn:aws:iam::346319152574:role/bot_ec2_reporting"
role_session_name = "temporarySession"



sts_client = boto3.client('sts')
try :
    response = sts_client.assume_role(RoleArn=role_arn, RoleSessionName=role_session_name)
    print (response)

except ClientError as e :
    error_code = e.response['Error']['Code']
    print(e)
    print (error_code)    


#ec2_client = boto3.client('ec2')
#response = ec2_client.describe_images(
#            ImageIds = ['ami-2f796554',]
#        )