import boto3
import json

REGION = "us-east-1"
INSTANCE_ID = "i-01fa750a5f857c372"

ec2 = boto3.client("ec2", region_name=REGION)

def lambda_handler(event, context):
    try:
        response = ec2.stop_instances(InstanceIds=[INSTANCE_ID])
        state = response["StoppingInstances"][0]["CurrentState"]["Name"]
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "POST,OPTIONS"
            },
            "body": json.dumps({
                "message": "EC2 stop request submitted",
                "instance_id": INSTANCE_ID,
                "state": state
            })
        }
    except Exception as error:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "POST,OPTIONS"
            },
            "body": json.dumps({"message": str(error)})
        }
