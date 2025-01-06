import boto3
import json

client = boto3.client('s3')

response = client.get_bucket_acl(
    Bucket='2025-harths-python-01'
)
#complete_json = response.json()
#print(complete_json)
