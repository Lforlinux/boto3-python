import argparse
import boto3
import time
import json
import pprint
# Create a boto3 CloudFormation client
cf = boto3.client('cloudformation')

# Set up the argument parser
parser = argparse.ArgumentParser()
parser.add_argument("stack_name", help="The name of the stack to detect drift for")
args = parser.parse_args()

# Get the name of the stack
stack_name = args.stack_name

# Check if the stack exists
try:
    cf.describe_stacks(StackName=stack_name)
except cf.exceptions.ClientError as e:
    error_message = e.response['Error']['Message']
    if error_message == 'Stack with id {stack_name} does not exist':
        print(f"Error: The stack {stack_name} does not exist.")
        exit()

# Detect drift for the stack
result = cf.detect_stack_drift(StackName=stack_name)

# Get the drift detection ID
drift_detection_id = result['StackDriftDetectionId']

# Wait for the drift detection to complete
while True:
    drift_status = cf.describe_stack_drift_detection_status(StackDriftDetectionId=drift_detection_id)['DetectionStatus']
    if drift_status == 'DETECTION_COMPLETE':
        break
    time.sleep(5)

# Describe the stack resource drifts
drifts = cf.describe_stack_resource_drifts(StackName=stack_name)

# Print the drift information for each resource in the stack
for drift in drifts['StackResourceDrifts']:
    print("Stack:", stack_name)
    print("Resource:", drift['LogicalResourceId'])
    print("Drift Status:", drift['StackResourceDriftStatus'])
    if drift['StackResourceDriftStatus'] != 'DELETED':
        expected_properties = drift['ExpectedProperties']
        actual_properties = drift['ActualProperties']
        json_object = json.loads(expected_properties)
        json_object1 = json.loads(actual_properties)
        json_formatted_str = json.dumps(json_object, indent=2)
        json_formatted_str1 = json.dumps(json_object1, indent=2)

        if expected_properties == actual_properties:
            print("Expected and actual properties match.")
        else:
            print("Expected Properties:", json_formatted_str)

            print("Actual Properties:", json_formatted_str1)
    print("\n")