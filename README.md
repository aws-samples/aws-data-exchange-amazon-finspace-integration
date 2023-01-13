## How to set-up a fully automated data pipeline from AWS Data Exchange to Amazon FinSpace

This repo provides the CloudFormation template to deploy the automated integration between Amazon Data Exchange and Amazon FinSpace. 

More details about this repo are available [in this blog](https://aws.amazon.com/blogs/industries/how-to-set-up-a-fully-automated-data-pipeline-from-aws-data-exchange-to-amazon-finspace/)

Abstract from blog: 

"In previous posts we’ve presented scenarios where [Amazon FinSpace](https://aws.amazon.com/finspace/) data analysis capabilities are used to address different use cases. For these analyses we used data available on [AWS Data Exchange](https://aws.amazon.com/data-exchange/) and on third-party data sources. Some examples of analysis are [what-if scenarios of trading strategies](https://aws.amazon.com/blogs/industries/how-to-run-what-if-scenarios-for-trading-strategies-with-amazon-finspace/), [ESG portfolio optimization](https://aws.amazon.com/blogs/industries/automated-and-personalized-asset-portfolio-optimization-combining-esg-and-financial-data-on-amazon-finspace/), and [Analyzing petabytes of trade and quote data](https://aws.amazon.com/blogs/big-data/analyzing-petabytes-of-trade-and-quote-data-with-amazon-finspace/).

One key aspect in these analyses is data availability in FinSpace. There are different options to access data using FinSpace: you can access data in-place from FinSpace or ingest data into FinSpace. In the latter case, you can do it both manually, using FinSpace web interface, and programmatically, using both FinSpace API or using FinSpace Jupyter notebooks.

[In a previous post](https://aws.amazon.com/blogs/industries/using-esg-data-from-aws-dataexchange-in-amazon-finspace/), we’ve explained how to ingest data into FinSpace programmatically and manually.

In this post, we’re showing how to quickly create a pipeline that inserts datasets from AWS Data Exchange into FinSpace. This pipeline also gives you the option to manage periodical updates, meaning that as soon as a data update is available in AWS Data Exchange, the data update is immediately pushed into FinSpace. 
Additionally, this integration is available with an Infrastructure-as-Code (IaC) approach, so you can one-click deploy the integration with the dataset of your choice.
"

This repo contains code and configurations described and used in blog mentioned above. 

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

