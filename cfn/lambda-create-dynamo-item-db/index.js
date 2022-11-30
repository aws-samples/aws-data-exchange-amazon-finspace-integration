const AWS = require("aws-sdk"); const response = require("cfn-response"); const docClient = new AWS.DynamoDB.DocumentClient(); exports.handler = function(event, context) {
  console.log(JSON.stringify(event,null,2));
  var params = {
    TableName: event.ResourceProperties.DynamoTableName,
    Item:{
        "s3DatasetBucketArn": "arn:aws:s3:::deutscheborse-20220511",
        "datasetDescription": "The Deutsche Börse Public Data Set consists of trade data aggregated to one minute intervals from the Eurex and Xetra trading systems. It provides the initial price, lowest price, highest price, final price and volume for every minute of the trading day, and for every tradeable security. If you need higher resolution data, including untraded price movements, please refer to our historical market data product here. Also, be sure to check out our developer's portal.",
        "datasetName": "deutscheborse",
        "finspaceChangesetType": "APPEND",
        "finspaceDatasetColumns": [
         {
          "columnDescription": "ISIN of the security",
          "columnName": "ISIN",
          "dataType": "STRING"
         },
         {
          "columnDescription": "The product market segment",
          "columnName": "MarketSegment",
          "dataType": "STRING"
         },
         {
          "columnDescription": "text",
          "columnName": "UnderlyingSymbol",
          "dataType": "STRING"
         },
         {
          "columnDescription": "text",
          "columnName": "UnderlyingISIN",
          "dataType": "STRING"
         },
         {
          "columnDescription": "Currency in which the product is traded",
          "columnName": "Currency",
          "dataType": "STRING"
         },
         {
          "columnDescription": "Type of security",
          "columnName": "SecurityType",
          "dataType": "STRING"
         },
         {
          "columnDescription": "Date",
          "columnName": "MaturityDate",
          "dataType": "DATE"
         },
         {
          "columnDescription": "Price",
          "columnName": "StrikePrice",
          "dataType": "DOUBLE"
         },
         {
          "columnDescription": "text",
          "columnName": "PutOrCall",
          "dataType": "STRING"
         },
         {
          "columnDescription": "text",
          "columnName": "MLEG",
          "dataType": "STRING"
         },
         {
          "columnDescription": "text",
          "columnName": "ContractGenerationNumber",
          "dataType": "INTEGER"
         },
         {
          "columnDescription": "Id of the security",
          "columnName": "SecurityID",
          "dataType": "DOUBLE"
         },
         {
          "columnDescription": "Timestamp",
          "columnName": "Date",
          "dataType": "DATE"
         },
         {
          "columnDescription": "Time",
          "columnName": "Time",
          "dataType": "DATETIME"
         },
         {
          "columnDescription": "Start price",
          "columnName": "StartPrice",
          "dataType": "FLOAT"
         },
         {
          "columnDescription": "The maximum price",
          "columnName": "MaxPrice",
          "dataType": "FLOAT"
         },
         {
          "columnDescription": "The minimum price",
          "columnName": "MinPrice",
          "dataType": "FLOAT"
         },
         {
          "columnDescription": "the end price",
          "columnName": "EndPrice",
          "dataType": "FLOAT"
         },
         {
          "columnDescription": "Num of contracts",
          "columnName": "NumberOfContracts",
          "dataType": "INTEGER"
         },
         {
          "columnDescription": "Num of trades",
          "columnName": "NumberOfTrades",
          "dataType": "INTEGER"
         }
        ],
        "finspaceDatasetId": "ilkipb1",
        "finspaceDatasetKeyColumns": [
         "string"
        ],
        "finspaceDatasetOwnerInfo": {
         "email": "darth@darkside.com",
         "name": "Darth Vader",
         "phoneNumber": "347666666666"
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
        "finspaceEnvironmentId": "a3aei7wm6rb4syizqikw27",
        "finspaceGroupId": "rsBEirwRD8YXwmG1gXJA9A",
        "finspaceLastChangesetId": "WsBZUxTxlEyX9jY4impOQw",
        "finspaceRegion": "us-east-1"
    }
};
docClient.put(params, function(err, data) { if (err) {
response.send(event, context, "FAILED", {});
} else {
response.send(event, context, "SUCCESS", {});
} }); };