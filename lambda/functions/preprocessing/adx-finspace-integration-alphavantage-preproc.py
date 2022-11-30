import json
import boto3
import pandas as pd
import datetime
import re
from botocore.exceptions import ClientError

from helpers import s3Helpers
from io import StringIO


def lambda_handler(event, context):
    # TODO implement preprocessing logic here
    
    s3Client = boto3.client('s3')
    s3_resource = boto3.resource('s3')
    
    
    s3BucketName = event ['s3BucketName'] 
    
    
    #only elements in the root will be considered
    response = s3Client.list_objects(Bucket=s3BucketName)
    

    df = pd.DataFrame()
    
    listOfSourceFiles = []
    
    for file in response["Contents"]:
        sourceFileName = file["Key"]
        obj = s3Client.get_object(Bucket=s3BucketName, Key=sourceFileName)
        obj_df = pd.read_csv(obj["Body"])
        substr = re.search('daily_adjusted_(.+?).csv', sourceFileName)
        if substr:
            ticker = substr.group(1)
        obj_df['ticker'] = ticker
        df = pd.concat([df, obj_df], ignore_index=True)
        listOfSourceFiles.append(sourceFileName)
    
    csv_buffer = StringIO()
    
    df.to_csv(csv_buffer, index=None, sep=",")
    
    now = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

    s3DatasetFilename = "_mergedDataset" + now + ".csv"
    
    print ("[INFO] - Dumping merged file " + s3DatasetFilename)
    
    s3_resource.Object(s3BucketName, s3DatasetFilename).put(Body=csv_buffer.getvalue())
    
    listOfSourceFiles.append(s3DatasetFilename)
    
    
    return {
        's3BucketArn': event['s3BucketArn'],
        's3BucketName': s3BucketName,
        's3Region': event['s3Region'],
        's3DatasetFilename': s3DatasetFilename,
        's3SourcesToBeArchived': listOfSourceFiles
    } 