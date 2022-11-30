import json
import boto3
import botocore

def get_finspace_API_client_programmatically (finspace_environment_id, finspace_region, credentials_duration_minutes=60):
    
    apiCredentials = boto3.client('finspace-data').get_programmatic_access_credentials(
        durationInMinutes=60,
        environmentId=finspace_environment_id
    )
    
    awsAccessKeyId=apiCredentials['credentials']['accessKeyId']
    awsSecretAccessKey=apiCredentials['credentials']['secretAccessKey']
    awsSessionToken=apiCredentials['credentials']['sessionToken']
    
    session = boto3.session.Session()
    finSpaceClient = session.client(
      region_name=finspace_region,
      service_name='finspace-data',
      aws_access_key_id=awsAccessKeyId,
      aws_secret_access_key=awsSecretAccessKey,
      aws_session_token=awsSessionToken
    )
    
    return finSpaceClient

def get_changeset_status (client, dataset_id: str, changeset_id: str):
    
    response = client.get_changeset(
        datasetId=dataset_id,
        changesetId=changeset_id
    )

    status = response['status']
    
    print ("[INFO] - Changeset status is: " + status)

    if status == 'SUCCESS':
        print("[INFO] - Changeset " + changeset_id + " for dataset " +  dataset_id + " successfully applied.")
        #TODO:
        # store the timestamp of the changeset on dynamo
    elif status == 'PENDING' or status == 'RUNNING':
        print("[INFO] - Changeset " + changeset_id + " for dataset " +  dataset_id + " still running...")
    else:
        print("[ERR] - Changeset " + changeset_id + " for dataset " +  dataset_id + " in error state.")
        print(response["errorInfo"])
        print(response["errorCategory"])
    
    return status

def apply_changeset_from_s3 (finspace_api_client, dataset_id, change_type, S3_dataset_source_path):
    
    
    response = finspace_api_client.create_changeset(
    #clientToken='string',
    datasetId=dataset_id,
    changeType=change_type, #'REPLACE'|'APPEND'|'MODIFY'
    sourceParams={'s3SourcePath':S3_dataset_source_path, 'sourceType':'S3'},
    formatParams={'formatType':'CSV','separator': ',', 'withHeader': 'true'}

    )
    return response
    

def create_finspace_dataset(finspace_api_client, dataset_name, group_id,dataset_permissions, dataset_schema, dataset_description, owner_info):
    
    response = finspace_api_client.create_dataset(
        #clientToken='string',
        datasetTitle=dataset_name,
        kind='TABULAR',
        datasetDescription=dataset_description,
        ownerInfo=owner_info,
        permissionGroupParams={
            'permissionGroupId': group_id,
            'datasetPermissions': dataset_permissions_helper(dataset_permissions)
        },
        #alias='string',
        schemaDefinition=dataset_schema
    )

    dataset_id = response["datasetId"]
    return dataset_id
    
    
def dataset_permissions_helper (requiredPermissions):
    request_dataset_permissions = [{"permission": permissionName} for permissionName in requiredPermissions]
    return request_dataset_permissions

def create_finspace_dataview(finspace_api_client, dataset_id):
    
    response = finspace_api_client.create_data_view(
        datasetId=dataset_id,
        autoUpdate=True,
        destinationTypeParams={
            'destinationType': 'S3',
            's3DestinationExportFileFormat': 'DELIMITED_TEXT',
            's3DestinationExportFileFormatOptions': { "header": "true", "delimiter": ",", "compression": "gzip" }
        }
    )
    
    return response["dataViewId"]