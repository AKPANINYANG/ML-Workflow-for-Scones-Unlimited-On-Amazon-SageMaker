# Import the necessary libraries
import json

# Specify the threshold value
THRESHOLD = .85

# Define a Lambda function handler
def lambda_handler(event, context):
    
    # Extract the inferences from the event
    inferences = event["inferences"]
    
    # Check if any values in our inferences are above the threshold
    meets_threshold = (max(inferences) > THRESHOLD)
    
    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        raise Exception("THRESHOLD_CONFIDENCE_NOT_MET")

    # Return a dictionary with the status code and event data
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
