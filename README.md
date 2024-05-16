# AWS Lambda Current Time Function

This repository contains a Lambda function that returns the current time in JSON format, along with the Terraform configuration needed to deploy it to AWS. It also integrates GitHub Actions for CI/CD, automating deployment on pushes to the main branch.

## Key Components

- **Lambda Function**: Returns the current time as JSON.
- **Terraform**: Used to create and manage AWS resources for the Lambda function.
- **GitHub Actions**: Automatically deploys updates to AWS when changes are pushed to the main branch.

## Setup and Deployment

1. **Environment Variables**: Necessary AWS credentials (access key and secret key) are securely stored in GitHub repository secrets.

2. **GitHub Actions**: The workflow for CI/CD is defined under `.github/workflows`, which handles the automated deployment of the Lambda function via Terraform.

3. **Deployment**: Changes pushed to the main branch trigger the GitHub Actions workflow, automatically deploying updates to AWS.

## Usage

Once deployed, the Lambda function can be invoked to return the current server time in the following JSON format:
```json
{ "currentTime": "YYYY-MM-DD HH:MM:SS" }