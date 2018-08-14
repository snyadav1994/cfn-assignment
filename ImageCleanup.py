import boto3
from botocore.exceptions import ClientError
import sys


role_arn = "arn:aws:iam::346319152574:role/travel-qa-deployment-role"
role_session_name = "temporarySession"



sts_client = boto3.client('sts')

response = sts_client.assume_role(RoleArn=role_arn, RoleSessionName=role_session_name)
    #print (response)
credentials = response['Credentials']
aws_access_key_id=credentials['AccessKeyId'],
aws_secret_access_key=credentials['SecretAccessKey'],
aws_session_token=credentials['SessionToken']
   
ec2_client = boto3.client('ec2',aws_access_key_id,aws_secret_access_key,aws_session_token)
res = ec2_client.describe_images(
            ImageIds = ['ami-00312917',]
        )
print (res['Images'])
