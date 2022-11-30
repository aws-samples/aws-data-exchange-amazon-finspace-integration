import json
import boto3
from botocore.exceptions import ClientError

def archive_processed_dataset (bucket_name, dataset_file_name, s3_client, processed_datasets_folder_name='_processed'):
    
    try:
        res = s3_client.copy_object(Bucket = bucket_name, 
            CopySource = bucket_name + '/' + dataset_file_name, 
            Key = processed_datasets_folder_name + '/' + dataset_file_name
        )
    
    except ClientError as e:
        print("[ERROR] - Failed to copy the dataset file " + dataset_file_name + e.response['Error']['Message'])
    
    else:
        
        try:
            response = s3_client.delete_object(
            Bucket=bucket_name,
            Key=dataset_file_name
        )
        except ClientError as e:
            print("[ERROR] - Failed to remove the original dataset file " + e.response['Error']['Message'])
        else:
            print ("[INFO] - Dataset file "+ dataset_file_name + " successfully archived to " + processed_datasets_folder_name + '/' + dataset_file_name +" deleting original file.")
    return

def extract_dataset_S3_path_from_event (input_event):
    
    s3Region = input_event ['s3Region']
    s3BucketName = input_event ['s3BucketName']
    s3DatasetFile = input_event ['s3DatasetFilename']
    
    s3 = boto3.resource('s3', region_name=s3Region)
    
    fullPath='https://' + s3BucketName + '.s3.' + s3Region + '.amazonaws.com/' + s3DatasetFile
    
    return fullPath
    
    
def extract_bucket_arn_from_eventbridge (eventbridge_event):    
    return eventbridge_event['resources'][0]
