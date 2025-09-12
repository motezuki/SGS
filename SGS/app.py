from dash import Dash, html

app = Dash(__name__,
        serve_locally=False,
        compress=False)
layout=[
    html.H1("Hello, Dash!"),
    html.Div("This is a simple Dash application running on AWS Lambda.")
]

app.layout = layout
