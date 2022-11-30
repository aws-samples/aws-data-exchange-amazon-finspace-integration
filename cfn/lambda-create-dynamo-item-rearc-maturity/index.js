const AWS = require("aws-sdk"); 
const response = require("cfn-response"); 
const docClient = new AWS.DynamoDB.DocumentClient(); 

exports.handler = function(event, context) {
  console.log(JSON.stringify(event,null,2));
  var datesetBucketArn = "arn:aws:s3:::" + event.ResourceProperties.S3RearcDataFilesBucket;
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
      "datasetDescription": "Federal Reserve Board's data download program provides free and open access to various financial and economic data. Treasury yield refers to the return on an investment in a U.S. government debt obligation, such as a bill, note or bond.",
      "datasetName": "Daily Treasury Maturities",
      "finspaceChangesetType": "REPLACE",
      "finspaceDatasetColumns": [
       {
        "columnDescription": "TimePeriod",
        "columnName": "TimePeriod",
        "dataType": "DATE"
       },
       {
        "columnDescription": "Market yield on U.S. Treasury securities at 1-month   constant maturity, quoted on investment basis",
        "columnName": "RIFLGFCM01_NB",
        "dataType": "FLOAT"
       },
       {
        "columnDescription": "Market yield on U.S. Treasury securities at 3-month   constant maturity, quoted on investment basis",
        "columnName": "RIFLGFCM03_NB",
        "dataType": "FLOAT"
       },
       {
        "columnDescription": "Market yield on U.S. Treasury securities at 6-month   constant maturity, quoted on investment basis",
        "columnName": "RIFLGFCM06_NB",
        "dataType": "FLOAT"
       },
       {
        "columnDescription": "Market yield on U.S. Treasury securities at 1-year   constant maturity, quoted on investment basis",
        "columnName": "RIFLGFCY01_NB",
        "dataType": "FLOAT"
       },
       {
        "columnDescription": "Market yield on U.S. Treasury securities at 2-year   constant maturity, quoted on investment basis",
        "columnName": "RIFLGFCY02_NB",
        "dataType": "FLOAT"
       },
       {
        "columnDescription": "Market yield on U.S. Treasury securities at 3-year   constant maturity, quoted on investment basis",
        "columnName": "RIFLGFCY03_NB",
        "dataType": "FLOAT"
       },
       {
        "columnDescription": "Market yield on U.S. Treasury securities at 5-year   constant maturity, quoted on investment basis",
        "columnName": "RIFLGFCY05_NB",
        "dataType": "FLOAT"
       },
       {
        "columnDescription": "Market yield on U.S. Treasury securities at 7-year   constant maturity, quoted on investment basis",
        "columnName": "RIFLGFCY07_NB",
        "dataType": "FLOAT"
       },
       {
        "columnDescription": "Market yield on U.S. Treasury securities at 10-year   constant maturity, quoted on investment basis",
        "columnName": "RIFLGFCY10_NB",
        "dataType": "FLOAT"
       },
       {
        "columnDescription": "Market yield on U.S. Treasury securities at 20-year   constant maturity, quoted on investment basis",
        "columnName": "RIFLGFCY20_NB",
        "dataType": "FLOAT"
       },
       {
        "columnDescription": "Market yield on U.S. Treasury securities at 30-year   constant maturity, quoted on investment basis",
        "columnName": "RIFLGFCY30_NB",
        "dataType": "FLOAT"
       }
      ],
      "finspaceDatasetId": "",
      "finspaceDatasetKeyColumns": [
       "TimePeriod"
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