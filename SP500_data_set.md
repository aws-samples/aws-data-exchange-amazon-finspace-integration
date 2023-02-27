# SP500-Dataset

This dataset contains a historical timeseries data of the S&P 500 stock market index. Data coverage starts from 2011-02-03 and is updated daily, at close of the day. The data is provided in the form of a single CSV file.
  
The data contains the following columns:

- DATE
- SP500
  
The values within the data field labeled `SP500` represent the daily index value at market close at the time of the corresponding `DATE` field. 


## Data pipeline to ingest data into Amazon FinSpace

The process to ingest this dataset is very similar to the one for `Daily Treasury Maturities | Federal Reserve Board from Rearc` present in the blog. This is because, like that dataset, this data does not require any preprocessing and is ready to be placed into FinSpace. As a result, only minor adjustments were required, and we were able to successfully reuse most of the code from that pipeline. 


