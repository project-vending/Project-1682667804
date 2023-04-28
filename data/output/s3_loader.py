python
import boto3

# Define S3 configuration
S3_BUCKET_NAME = "your_bucket_name"
S3_PREFIX = "output"

# Define a function to upload files to S3
def upload_to_s3(file_path, s3_key):
    s3 = boto3.client("s3")
    s3.upload_file(file_path, S3_BUCKET_NAME, f"{S3_PREFIX}/{s3_key}")
    print(f"{file_path} uploaded to {S3_BUCKET_NAME}/{S3_PREFIX}/{s3_key}")

# Define a function to download files from S3
def download_from_s3(s3_key, file_path):
    s3 = boto3.client("s3")
    s3.download_file(S3_BUCKET_NAME, f"{S3_PREFIX}/{s3_key}", file_path)
    print(f"{S3_BUCKET_NAME}/{S3_PREFIX}/{s3_key} downloaded to {file_path}")

# Example usage
if __name__ == "__main__":
    file_path = "data/output/test.txt"
    s3_key = "test.txt"
    upload_to_s3(file_path, s3_key)
    download_from_s3(s3_key, file_path)
