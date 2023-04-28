python
import os
import boto3

# Define the S3 bucket and object key for your data
BUCKET_NAME = 'your-bucket-name'
OBJECT_KEY = 'path/to/your/data.csv'

# Create a boto3 S3 client
s3_client = boto3.client('s3')

# Download the data from S3 and save it to the data/raw directory
os.makedirs('data/raw', exist_ok=True)
with open('data/raw/data.csv', 'wb') as f:
    s3_client.download_fileobj(BUCKET_NAME, OBJECT_KEY, f)
    
print(f"Data downloaded from S3 bucket {BUCKET_NAME} and saved to data/raw/data.csv")
