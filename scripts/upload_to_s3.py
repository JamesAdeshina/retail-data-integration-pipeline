import boto3
import os
from dotenv import load_dotenv

# Load credentials from config/.env
load_dotenv("config/.env")

# Initialize S3 client
s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION")
)

bucket_name = os.getenv("S3_BUCKET_NAME")
local_root = "data/raw"

def upload_files_to_s3(local_root, bucket_name):
    """
    Walks through local folder structure and uploads every file
    to the same structure in S3 under the 'bronze' prefix.
    """
    for root, _, files in os.walk(local_root):
        for file in files:
            local_path = os.path.join(root, file)
            relative_path = os.path.relpath(local_path, local_root)
            s3_key = f"bronze/{relative_path.replace(os.sep, '/')}"
            s3.upload_file(local_path, bucket_name, s3_key)
            print(f"Uploaded: s3://{bucket_name}/{s3_key}")

if __name__ == "__main__":
    print("Uploading files to S3...")
    upload_files_to_s3(local_root, bucket_name)
    print("All files uploaded successfully!")
