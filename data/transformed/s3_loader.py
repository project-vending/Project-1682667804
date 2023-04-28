python
import boto3

# Define the S3 bucket name and file key
BUCKET_NAME = 'my-s3-bucket'
FILE_KEY = 'my-transformed-data.csv'

# Define the function to upload the transformed data to S3
def upload_to_s3(data):
    s3_client = boto3.client('s3')
    s3_client.put_object(Bucket=BUCKET_NAME, Key=FILE_KEY, Body=data)

# Test the function with some sample data
if __name__ == '__main__':
    sample_data = 'Name,Age,Salary\nJohn,30,50000\nJane,25,60000'
    upload_to_s3(sample_data.encode('utf-8'))
