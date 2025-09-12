import json
import serverless_wsgi
from dash import Dash
from sgs import build_page

app = Dash(__name__,
        serve_locally=False,
        compress=False)

def lambda_handler(event, context):
    # Log the incoming event
    print("Received event:", json.dumps(event))
    print("Received context:", json.dumps(context))

    # Your business logic goes here
    return serverless_wsgi.handle_request(app.server, event, context)

if __name__ == "__main__":
    build_page(app)
    app.run(debug=True)
