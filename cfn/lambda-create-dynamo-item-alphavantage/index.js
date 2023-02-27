const AWS = require("aws-sdk"); 
const response = require("cfn-response"); 
const docClient = new AWS.DynamoDB.DocumentClient(); 

exports.handler = function(event, context) {
  console.log(JSON.stringify(event,null,2));
  var datesetBucketArn = "arn:aws:s3:::" + event.ResourceProperties.S3AVDataFilesBucket;
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
      "datasetDescription": "This free dataset contains 20+ years of end-of-day historical data for the top 10 US companies by market cap as of September 5, 2020. Data is delivered in CSV format.",
      "datasetName": "20 Years of End-of-Day Stock Data for Top 10 US Companies by Market Cap",
      "finspaceChangesetType": "REPLACE",
      "finspaceDatasetColumns": [
        {
          "columnDescription": "The timestamp of the eod",
          "columnName": "timestamp",
          "dataType": "DATE"
        },
        {
          "columnDescription": "The open value",
          "columnName": "open",
          "dataType": "FLOAT"
        },
        {
          "columnDescription": "The highest value",
          "columnName": "high",
          "dataType": "FLOAT"
        },
        {
          "columnDescription": "The lowest value",
          "columnName": "low",
          "dataType": "FLOAT"
        },
        {
          "columnDescription": "The close value",
          "columnName": "close",
          "dataType": "FLOAT"
        },
        {
          "columnDescription": "The adjuted close value",
          "columnName": "adjusted_close",
          "dataType": "FLOAT"
        },
        {
          "columnDescription": "The volume",
          "columnName": "volume",
          "dataType": "FLOAT"
        },
        {
          "columnDescription": "The split coefficient ",
          "columnName": "split_coefficient",
          "dataType": "FLOAT"
        },
        {
          "columnDescription": "The dividend amount",
          "columnName": "dividend_amount",
          "dataType": "FLOAT"
        },
        {
         "columnDescription": "The company ticker",
         "columnName": "ticker",
         "dataType": "FLOAT"
        }
      ],
      "finspaceDatasetId": "",
      "finspaceDatasetKeyColumns": [
        "timestamp"
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