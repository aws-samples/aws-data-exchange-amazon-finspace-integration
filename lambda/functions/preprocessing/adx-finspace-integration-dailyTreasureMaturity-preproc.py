import json
import boto3
import pandas as pd
import datetime

from io import StringIO
from botocore.exceptions import ClientError


def lambda_handler(event, context):
    # TODO implement preprocessing logic here
    
    s3Client = boto3.client('s3')
    s3_resource = boto3.resource('s3')
    
    s3BucketName = event ['detail']['bucket']['name'] 
    sourceFileName = event ['detail']['object']['key']
    
    #only elements in the root will be considered
    response = s3Client.list_objects(Bucket=s3BucketName, Delimiter="/")

    csv_buffer = StringIO()
    listOfSourceFiles = []
    
    obj = s3Client.get_object(Bucket=s3BucketName, Key=sourceFileName)
    
    print ("[INFO] - Reading input file: " + sourceFileName)
    
    obj_df = pd.read_csv(obj["Body"],skiprows=5)
    
    #obj_df = obj_df.replace('ND',0)
    
    for header in (list(obj_df.columns.values)):
        obj_df.rename(columns={header: header.replace(".","")}, inplace=True)
        obj_df.rename(columns={header: header.replace(" ","")}, inplace=True)
    
    #obj_df.to_csv(csv_buffer,index=False,na_rep=0)
    obj_df.to_csv(csv_buffer,index=False)
    
    now = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    
    s3DatasetFilename = "_temp/preprocDailyTreasureDataset" + now + ".csv"
    
    print ("[INFO] - Dumping preprocessed file " + s3DatasetFilename)
    
    s3_resource.Object(s3BucketName, s3DatasetFilename).put(Body=csv_buffer.getvalue())
    
    listOfSourceFiles.append(s3DatasetFilename)
    listOfSourceFiles.append(sourceFileName)
    
    return {
        's3BucketArn': event['resources'][0],
        's3BucketName': s3BucketName,
        's3Region': event['region'],
        's3DatasetFilename': s3DatasetFilename,
        's3SourcesToBeArchived': listOfSourceFiles
    } 