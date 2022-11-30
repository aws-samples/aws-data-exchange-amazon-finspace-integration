import json
import boto3
from helpers import s3Helpers
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    
    S3bucketName = event['s3BucketName']
    s3FilesToBeArchived = event['s3SourcesToBeArchived']
    
    s3client = boto3.client('s3')
    
    for file in s3FilesToBeArchived:
        s3Helpers.archive_processed_dataset(S3bucketName, file, s3client)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
