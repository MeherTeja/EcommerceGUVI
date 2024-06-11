# EcommerceGUVI

As an e-commerce company, our success hinges on seamlessly integrating our online platform with efficient logistics management to ensure optimal customer satisfaction and operational efficiency. To achieve this synergy, we aim to leverage real-time data streams from both our website and fleet of delivery trucks. 

Online Platform Optimization:

We need to analyze clickstream data to understand customer preferences, enhance user experience, and optimize marketing strategies for key product categories such as mobile phones, laptops, and cameras.

Data Processors:
AWS Kinesis: Real-time data streaming and processing for both clickstream data and truck IoT sensor data.
AWS Lambda: Further analysis and computation of insights for both data streams.

Data Destinations:
Snowflake or DynamoDB: Store the processed clickstream data and truck IoT sensor data for historical analysis, reporting, and integration with other business systems.
For the truck data the schema should follow Type 2 SCD(Slowly changing dimensions) , we need historical data of the truck every time it send the data
