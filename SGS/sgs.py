from dash import html

layout=[
    html.H1("Hello, Dash!"),
    html.Div("This is a simple Dash application running on AWS Lambda.")
]

def build_page(app):
    app.layout = layout
    return