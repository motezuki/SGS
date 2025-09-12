import json


def lambda_handler(event, context):
    # Log the incoming event
    print("Received event:", json.dumps(event))

    # Your business logic goes here

    return {"statusCode": 200, "body": json.dumps({"message": "Hello from SGS!"})}
