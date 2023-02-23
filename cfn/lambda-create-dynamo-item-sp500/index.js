const AWS = require("aws-sdk"); 
const response = require("cfn-response"); 
const docClient = new AWS.DynamoDB.DocumentClient(); 

exports.handler = function(event, context) {
  console.log(JSON.stringify(event,null,2));
  var datesetBucketArn = "arn:aws:s3:::" + event.ResourceProperties.S3SP500FilesBucket;
  var datasetOwnerEmail = event.ResourceProperties.FinspaceDatasetOwnerEmail;
  var datasetOwnerName = event.ResourceProperties.FinspaceDatasetOwnerName;
  var datasetOwnerPhone = event.ResourceProperties.FinspaceDatasetOwnerPhone;
  var finspaceDomainId = event.ResourceProperties.FinspaceDomainId;
  var finspaceGroupId = event.ResourceProperties.FinspaceGroupId;
  var finspaceRegion = event.ResourceProperties.FinspaceRegion;
  
  var params = {
    TableName: event.ResourceProperties.DynamoTableName,
    Item:{
      "s3DatasetBucketArn": datesetBucketArn,
      "datasetDescription": "This dataset contains a historical time-series data of S&P Dow Jones Indices LLC, S&P 500 (SP500) retrieved from the Federal Reserve Bank of St. Louis Economic Data (FRED) at https://fred.stlouisfed.org/series/SP500. Data coverage starts from 2011-02-03. ",
      "datasetName": "S&P 500 (SP500) | FRED",
      "finspaceChangesetType": "REPLACE",
      "finspaceDatasetColumns": [
       {
        "columnDescription": "Date",
        "columnName": "DATE",
        "dataType": "DATE"
       },
       {
        "columnDescription": "SP500 index value",
        "columnName": "SP500",
        "dataType": "FLOAT"
       }
      ],
      "finspaceDatasetId": "",
      "finspaceDatasetKeyColumns": [
       "DATE"
      ],
      "finspaceDatasetOwnerInfo": {
        "email": datasetOwnerEmail,
        "name": datasetOwnerName,
        "phoneNumber": datasetOwnerPhone
       },
       
      "finspaceDatasetPermissions": [
       "ViewDatasetDetails",
       "ReadDatasetData",
       "AddDatasetData",
       "CreateSnapshot",
       "EditDatasetMetadata",
       "ManageDatasetPermissions",
       "DeleteDataset"
      ],
      "finspaceEnvironmentId": finspaceDomainId,
      "finspaceGroupId": finspaceGroupId,
      "finspaceLastChangesetId": "",
      "finspaceRegion": finspaceRegion
     }
};
docClient.put(params, function(err, data) { if (err) {
response.send(event, context, "FAILED", {});
} else {
response.send(event, context, "SUCCESS", {});
} }); };