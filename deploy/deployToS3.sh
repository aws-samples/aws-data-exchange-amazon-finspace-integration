#!/bin/bash

if [ $# -eq 0 ]
  then
    echo "Please provide the s3 target bucket as first argument!"
    exit 1
fi


echo "Deploying to S3 bucket: $1"

rm -rf ./artifacts/*

#lambda function packaging
zip -j ./artifacts/checkFinspaceStatus.py.zip ../lambda/functions/checkFinspaceStatus/checkFinspaceStatus.py
zip -j ./artifacts/importDataset.py.zip ../lambda/functions/importDataset/importDataset.py
zip -j ./artifacts/postprocessing.py.zip ../lambda/functions/postprocessing/postprocessing.py
zip -j ./artifacts/adx-finspace-integration-alphavantage-preproc.zip ../lambda/functions/preprocessing/adx-finspace-integration-alphavantage-preproc.py
zip -j ./artifacts/adx-finspace-integration-dailyTreasureMaturity-preproc.zip ../lambda/functions/preprocessing/adx-finspace-integration-dailyTreasureMaturity-preproc.py
zip -j ./artifacts/adx-finspace-integration-sp500-preproc.zip ../lambda/functions/preprocessing/adx-finspace-integration-sp500-preproc.py

#cfn templates packaging
cp ../cfn/adx-cfn-core.json ./artifacts/
cp ../cfn/adx-cfn-rearc.json ./artifacts/
cp ../cfn/adx-cfn-alphavantage.json ./artifacts/

#state machine packaging
cp ../stepFunctions/stateMachine-template.json ./artifacts/stateMachine-template.json

#lambda layer packaging
cp -r ../lambda/layer/python ./artifacts/
cd ./artifacts/
zip -r lambda_layer_python_adx_finspace.zip python
rm -rf python/
cd ..

#helpers functions to create dynamodb items for alphavantage
cp -r ../cfn/lambda-create-dynamo-item-alphavantage ./artifacts/
cd ./artifacts/lambda-create-dynamo-item-alphavantage
zip -r lambda-create-dynamo-item-alphavantage.zip cfn-response.js index.js node_modules/
mv lambda-create-dynamo-item-alphavantage.zip ..
cd ..
rm -rf lambda-create-dynamo-item-alphavantage
cd ..

#helpers functions to create dynamodb items for rearc maturity
cp -r ../cfn/lambda-create-dynamo-item-rearc-maturity ./artifacts/
cd ./artifacts/lambda-create-dynamo-item-rearc-maturity
zip -r lambda-create-dynamo-item-rearc-maturity.zip cfn-response.js index.js node_modules/
mv lambda-create-dynamo-item-rearc-maturity.zip ..
cd ..
rm -rf lambda-create-dynamo-item-rearc-maturity
cd ..

#helpers functions to create dynamodb items for SP500
cp -r ../cfn/lambda-create-dynamo-item-sp500 ./artifacts/
cd ./artifacts/lambda-create-dynamo-item-sp500
zip -r lambda-create-dynamo-item-sp500.zip cfn-response.js index.js node_modules/
mv lambda-create-dynamo-item-sp500.zip ..
cd ..
rm -rf lambda-create-dynamo-item-sp500

#clean up the target bucket (versioning disabled)
aws s3 rm s3://$1 --recursive

#deploy new files
aws s3 sync . s3://$1