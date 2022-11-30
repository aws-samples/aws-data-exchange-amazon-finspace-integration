from botocore.exceptions import ClientError
import boto3
import json

def get_finspace_environmentId (dataset_bucket_arn, table_name='ADX'): 
    
 
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table(table_name)
    
    try:
        response = table.get_item(
            Key={'s3DatasetBucketArn': dataset_bucket_arn},
            ProjectionExpression='finspaceEnvironmentId'
            )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']['finspaceEnvironmentId']


def get_finspace_region (dataset_bucket_arn, table_name='ADX'):

    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table(table_name)

    try:
        response = table.get_item(
            Key={'s3DatasetBucketArn': dataset_bucket_arn},
            ProjectionExpression='finspaceRegion'
            )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']['finspaceRegion']


def get_finspace_changeset_type (dataset_bucket_arn, table_name='ADX'):

    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table(table_name)

    try:
        response = table.get_item(
            Key={'s3DatasetBucketArn': dataset_bucket_arn},
            ProjectionExpression='finspaceChangesetType'
            )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']['finspaceChangesetType']


def get_finspace_datasetId (dataset_bucket_arn, table_name='ADX'):

    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table(table_name)

    try:
        response = table.get_item(
            Key={'s3DatasetBucketArn': dataset_bucket_arn},
            ProjectionExpression='finspaceDatasetId'
            )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']['finspaceDatasetId']
        


def get_dataset_name (dataset_bucket_arn, table_name='ADX'):

    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table(table_name)

    try:
        response = table.get_item(
            Key={'s3DatasetBucketArn': dataset_bucket_arn},
            ProjectionExpression='datasetName'
            )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']['datasetName']


def get_finspace_groupId (dataset_bucket_arn, table_name='ADX'):

    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table(table_name)

    try:
        response = table.get_item(
            Key={'s3DatasetBucketArn': dataset_bucket_arn},
            ProjectionExpression='finspaceGroupId'
            )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']['finspaceGroupId']
        
        
def get_dataset_description (dataset_bucket_arn, table_name='ADX'):

    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table(table_name)

    try:
        response = table.get_item(
            Key={'s3DatasetBucketArn': dataset_bucket_arn},
            ProjectionExpression='datasetDescription'
            )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']['datasetDescription']
        
        
def store_finspace_datasetId (dataset_id, dataset_bucket_arn, table_name='ADX'):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    try:
        response = table.update_item(
        Key={
            's3DatasetBucketArn': dataset_bucket_arn
        },
        UpdateExpression="set finspaceDatasetId = :val",
        ExpressionAttributeValues={':val': dataset_id},
        ReturnValues="UPDATED_NEW"
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response
        
def store_finspace_last_changesetId (changeset_id, dataset_bucket_arn, table_name='ADX'):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    try:
        response = table.update_item(
        Key={
            's3DatasetBucketArn': dataset_bucket_arn
        },
        UpdateExpression="set finspaceLastChangesetId = :val",
        ExpressionAttributeValues={':val': changeset_id},
        ReturnValues="UPDATED_NEW"
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response
        
def get_finspace_dataset_permissions(dataset_bucket_arn, table_name='ADX'):
    database = boto3.resource('dynamodb')
    table = database.Table(table_name)
    res = table.get_item(Key = {'s3DatasetBucketArn':dataset_bucket_arn}, ProjectionExpression = "finspaceDatasetPermissions")
    return res['Item']['finspaceDatasetPermissions']
    
    
def get_dataset_owner_info(dataset_bucket_arn, table_name='ADX'):
    database = boto3.resource('dynamodb')
    table = database.Table(table_name)
    res = table.get_item(Key = {'s3DatasetBucketArn':dataset_bucket_arn}, ProjectionExpression = "finspaceDatasetOwnerInfo")
    return res['Item']['finspaceDatasetOwnerInfo']
    
    
def get_finspace_dataset_columns(dataset_bucket_arn, table_name='ADX'):
    database = boto3.resource('dynamodb')
    table = database.Table('ADX')
    res = table.get_item(Key = {'s3DatasetBucketArn':dataset_bucket_arn}, ProjectionExpression = "finspaceDatasetColumns")
    return res ['Item']['finspaceDatasetColumns']
    
def get_finspace_dataset_primary_keys_list (dataset_bucket_arn, table_name='ADX'):
    database = boto3.resource('dynamodb')
    table = database.Table('ADX')
    res = table.get_item(Key = {'s3DatasetBucketArn':dataset_bucket_arn}, ProjectionExpression = "finspaceDatasetKeyColumns")
    return res ['Item']['finspaceDatasetKeyColumns']

def build_dataset_tabularSchemaConfig(dataset_bucket_arn):
    columnsList = get_finspace_dataset_columns(dataset_bucket_arn)
    primaryKeysList = get_finspace_dataset_primary_keys_list(dataset_bucket_arn)
    returnedObject =  '{"tabularSchemaConfig":{"columns":' + json.dumps(columnsList) + ',"primaryKeyColumns":' + json.dumps(primaryKeysList) + '}}'
    return json.loads(returnedObject)