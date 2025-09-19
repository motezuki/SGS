import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# import json
import serverless_wsgi
from SGS.app import app

def lambda_handler(event, context):
    # Log the incoming event
    # print("Received event:", json.dumps(event))
    # print("Received context:", json.dumps(context))

    return serverless_wsgi.handle_request(app.server, event, context)
