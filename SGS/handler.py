import json
import serverless_wsgi
from dash import Dash
from app import app

def lambda_handler(event, context):
    # Log the incoming event
    print("Received event:", json.dumps(event))
    print("Received context:", json.dumps(context))

    return serverless_wsgi.handle_request(app.server, event, context)
