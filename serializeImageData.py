# Import the necessary libraries
import json
import boto3
import base64

# Instantiate a boto3 resource for S3
s3 = boto3.resource('s3')

# Define a Lambda function handler
def lambda_handler(event, context):
    """A function to serialize target data from S3"""
    
    # Extract the S3 key and bucket name from the event
    key = event['s3_key']
    bucket = event['s3_bucket']
    
    # Download the file from S3 to a local file
    s3.Bucket(bucket).download_file(key, '/tmp/image.png')

    # Open the local file in binary mode and read its contents
    with open("/tmp/image.png", "rb") as f:
        # Encode the file contents as base64
        image_data = base64.b64encode(f.read())

    # Print the keys of the event dictionary
    print("Event:", event.keys())

    # Return a dictionary with the status code, image data, S3 bucket name, S3 key, and an empty list of inferences
    return {
        'statusCode': 200,
        'body': {
            "image_data": image_data,
            "s3_bucket": bucket,
            "s3_key": key,
            "inferences": []
        }
    }
