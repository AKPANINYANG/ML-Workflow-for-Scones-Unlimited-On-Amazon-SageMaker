# Import the necessary libraries
import os
import io
import boto3
import json
import base64

# Specify the name of your deployed model
ENDPOINT = 'image-classification-2023-01-18-19-42-56-366'

# Instantiate a SageMaker runtime client
runtime= boto3.client('sagemaker-runtime')

# Define a Lambda function handler
def lambda_handler(event, context):

    # Decode the image data from the event body
    image = base64.b64decode(event["body"]["image_data"])

    # Invoke the SageMaker endpoint with the image data
    response = runtime.invoke_endpoint(
        EndpointName=ENDPOINT,
        Body=image,
        ContentType='image/png'
    )
    
    # Decode the response and extract the inferences
    decode_response = response['Body'].read().decode('utf-8')
    inferences = [float(x) for x in decode_response[1:-1].split(',')]

    # Return a dictionary with the status code and inferences
    return {
        'statusCode': 200,
        'inferences': inferences
    }
