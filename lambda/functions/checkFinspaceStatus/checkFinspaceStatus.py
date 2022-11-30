import json
import boto3
from helpers import dynamoDbHelpers
from helpers import finspaceHelpers
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    
    finspaceRegion = event['finspaceRegion']
    datasetId = event['datasetId']
    changesetId = event['changesetId']
    s3DatasetBucketArn = event['s3BucketArn']
    
    finspaceApiClient = finspaceHelpers.get_finspace_API_client_programmatically(dynamoDbHelpers.get_finspace_environmentId(s3DatasetBucketArn), finspaceRegion)
    
    print ("[INFO] - Getting status for datasetid: " + datasetId + " changeset id: " + changesetId + " of dataset in bucket: " + s3DatasetBucketArn)
    
    changesetIngestionStatus = finspaceHelpers.get_changeset_status(finspaceApiClient, datasetId, changesetId)
    
    return {
        'datasetId': datasetId,
        'finspaceRegion': finspaceRegion,
        'changesetId': changesetId,
        's3BucketArn': s3DatasetBucketArn,
        'changesetStatus': changesetIngestionStatus,
        's3BucketName': event['s3BucketName'],
        's3DatasetFilename': event['s3DatasetFilename'],
        's3SourcesToBeArchived':event['s3SourcesToBeArchived']
        
    }


        



