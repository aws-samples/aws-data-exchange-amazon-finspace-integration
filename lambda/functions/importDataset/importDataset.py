import json
import boto3

from helpers import s3Helpers
from helpers import dynamoDbHelpers
from helpers import finspaceHelpers
from botocore.exceptions import ClientError           

def lambda_handler(event, context):
    
    s3DatasetBucketArn = event['s3BucketArn']
    
    datasetfile = s3Helpers.extract_dataset_S3_path_from_event(event)

    print ("[INFO] - Start import of dataset: " + datasetfile + " from bucket: " + s3DatasetBucketArn )
    
    finspaceRegion = dynamoDbHelpers.get_finspace_region(s3DatasetBucketArn)

    #TODO: check if the bucket region is the same of finspace, otherwise abort
    finspace_api_client = finspaceHelpers.get_finspace_API_client_programmatically(dynamoDbHelpers.get_finspace_environmentId(s3DatasetBucketArn), finspaceRegion)

    finspaceDatasetId = dynamoDbHelpers.get_finspace_datasetId(s3DatasetBucketArn)
    
    if not finspaceDatasetId:
        print ("[INFO] - DatasetId does not exist, let's create it" )
        #finspace dataset not created, let's create it and store the id on dynamodb
        try: 
            finspaceDatasetId = finspaceHelpers.create_finspace_dataset(finspace_api_client, dynamoDbHelpers.get_dataset_name(s3DatasetBucketArn), dynamoDbHelpers.get_finspace_groupId(s3DatasetBucketArn), dynamoDbHelpers.get_finspace_dataset_permissions(s3DatasetBucketArn), dynamoDbHelpers.build_dataset_tabularSchemaConfig(s3DatasetBucketArn), dynamoDbHelpers.get_dataset_description(s3DatasetBucketArn), dynamoDbHelpers.get_dataset_owner_info(s3DatasetBucketArn))
            
        except ClientError as e:
            print ("[ERROR] - Error creating dataset on finspace.")
            print(e.response['Error']['Message'])
        
        else:
            print ("[INFO] - Storing datasetid: " + finspaceDatasetId + " for bucket: " + s3DatasetBucketArn + " on dynamodb")
            dynamoDbHelpers.store_finspace_datasetId(finspaceDatasetId, s3DatasetBucketArn)
            print ("[INFO] - Create dataview for datasetid: " + finspaceDatasetId)
            try:
                finspaceDataView = finspaceHelpers.create_finspace_dataview(finspace_api_client,finspaceDatasetId)
            
            except ClientError as e:
                print ("[ERROR] - Error creating dataview on finspace for datasetid: " + finspaceDatasetId)
                print(e.response['Error']['Message'])
            
            else:
                print ("[INFO] - Data view " + finspaceDataView + " successfully created.")

    else:
        print ("[INFO] - DatasetId already exists on finspace: " + finspaceDatasetId + " no need to create it." )
        
    # here: datasetid has been retrieved or created on finspace
    
    finspaceChangeSetId = finspaceHelpers.apply_changeset_from_s3 (finspace_api_client, finspaceDatasetId, dynamoDbHelpers.get_finspace_changeset_type(s3DatasetBucketArn), datasetfile)['changesetId']
    
    print ("[INFO] - Changeset in progress: " + finspaceChangeSetId + " for datasetid: " + finspaceDatasetId)
    
    dynamoDbHelpers.store_finspace_last_changesetId(finspaceChangeSetId, s3DatasetBucketArn)
    
    
    return {
        'datasetId': finspaceDatasetId,
        'finspaceRegion': finspaceRegion,
        'changesetId': finspaceChangeSetId,
        's3BucketArn': s3DatasetBucketArn,
        's3BucketName': event['s3BucketName'],
        's3DatasetFilename': event['s3DatasetFilename'],
        's3SourcesToBeArchived':event['s3SourcesToBeArchived']
    }
    
    s3DatasetBucketArn = event['s3BucketArn']
    
    datasetfile = s3Helpers.extract_dataset_S3_path_from_event(event)

    print ("[INFO] - Start import of dataset: " + datasetfile + " from bucket: " + s3DatasetBucketArn )
    
    finspaceRegion = dynamoDbHelpers.get_finspace_region(s3DatasetBucketArn)

    #TODO: check if the bucket region is the same of finspace, otherwise abort
    finspace_api_client = finspaceHelpers.get_finspace_API_client_programmatically(dynamoDbHelpers.get_finspace_environmentId(s3DatasetBucketArn), finspaceRegion)

    finspaceDatasetId = dynamoDbHelpers.get_finspace_datasetId(s3DatasetBucketArn)
    
    if not finspaceDatasetId:
        print ("[INFO] - DatasetId does not exist, let's create it" )
        #finspace dataset not created, let's create it and store the id on dynamodb
        finspaceDatasetId = finspaceHelpers.create_finspace_dataset(finspace_api_client, dynamoDbHelpers.get_dataset_name(s3DatasetBucketArn), dynamoDbHelpers.get_finspace_groupId(s3DatasetBucketArn), dynamoDbHelpers.get_finspace_dataset_permissions(s3DatasetBucketArn), dynamoDbHelpers.build_dataset_tabularSchemaConfig(s3DatasetBucketArn), dynamoDbHelpers.get_dataset_description(s3DatasetBucketArn), dynamoDbHelpers.get_dataset_owner_info(s3DatasetBucketArn))
        print ("[INFO] - Storing datasetid: " + finspaceDatasetId + " for bucket: " + s3DatasetBucketArn + " on dynamodb")
        dynamoDbHelpers.store_finspace_datasetId(finspaceDatasetId, s3DatasetBucketArn)
    else:
        print ("[INFO] - DatasetId already exists on finspace: " + finspaceDatasetId + " no need to create it." )
        
    # here: datasetid has been retrieved or created on finspace
    
    finspaceChangeSetId = finspaceHelpers.apply_changeset_from_s3 (finspace_api_client, finspaceDatasetId, dynamoDbHelpers.get_finspace_changeset_type(s3DatasetBucketArn), datasetfile)['changesetId']
    
    print ("[INFO] - Changeset in progress: " + finspaceChangeSetId + " for datasetid: " + finspaceDatasetId)
    
    dynamoDbHelpers.store_finspace_last_changesetId(finspaceChangeSetId, s3DatasetBucketArn)
    
    return {
        'datasetId': finspaceDatasetId,
        'finspaceRegion': finspaceRegion,
        'changesetId': finspaceChangeSetId,
        's3BucketArn': s3DatasetBucketArn,
        's3BucketName': event['s3BucketName'],
        's3DatasetFilename': event['s3DatasetFilename'],
        's3SourcesToBeArchived':event['s3SourcesToBeArchived']
    }







