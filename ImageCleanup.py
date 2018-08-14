import boto3
from botocore.exceptions import ClientError
import sys

   
ec2_client = boto3.client('ec2',region_name="us-east-1")
res = ec2_client.describe_images(
            ImageIds = ['ami-2f796554',]
        )
print (res['Images'])
