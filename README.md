
# Build a ML Workflow For Scones Unlimited On Amazon SageMaker

This project demonstrates the creation of a machine learning workflow for Scones Unlimited using Amazon SageMaker. The workflow includes training an image classification model, deploying it as an API endpoint, and implementing serverless architecture using AWS Lambda functions and Step Functions. Additionally, Model Monitor is used to monitor the deployed model for errors.

## Project Overview
The project consists of the following steps:
1. Set up a SageMaker Studio workspace.
2. Perform ETL (extract, transform, load) to prepare the data for machine learning.
3. Train an image classification model using SageMaker's built-in algorithm.
4. Deploy the trained model as an API endpoint.
5. Create AWS Lambda functions for image classification and filtering low-confidence inferences.
6. Compose the Lambda functions together in a Step Function.
7. Monitor the deployed model using Model Monitor.

## Project Structure
The project repository is structured as follows:
- `notebooks/`: Contains Jupyter notebooks for each step of the project.
- `lambda_functions/`: Includes the code for the Lambda functions.
- `step_function/`: Contains the JSON export of the Step Function.
- `data/`: Contains the dataset used for training the model.
- `images/`: Includes sample images for making predictions.

## Getting Started
To get started with the project, follow these steps:
1. Set up a SageMaker Studio workspace.
2. Open the Jupyter notebooks in the `notebooks/` directory and execute each cell to run the code.
3. Follow the instructions in the notebooks to complete the ETL, training, deployment, Lambda function creation, and Step Function composition.
4. Monitor the deployed model using Model Monitor.
5. Customize the project as needed and experiment with different configurations.

## Dependencies
The project requires the following dependencies:
- Amazon SageMaker
- AWS Lambda
- AWS Step Functions
- AWS S3
- Python
- Jupyter Notebook

Make sure you have the necessary credentials and permissions to access the AWS services.

## License
This project is licensed under the MIT License.

## Acknowledgements
This project was completed as part of the Machine Learning Fundamentals Nanodegree program at Udacity.
The starter code and project rubric were provided by Udacity.