import sys
import os
import json
import pytest
from pytest_mock import MockerFixture
from dash import Dash

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../SGS')))
from handler import lambda_handler
from app import app

@pytest.mark.parametrize("method, expected_output",
                          [("GET", 200),
                           ("POST", 405),
                           ("PUT", 405), 
                           ("DELETE", 405)])
def test_lambda_handler(method, expected_output):
    event = {
        "httpMethod": method,
        "path": "/",
        "headers": {},
        "body": None
    }
    context = {}
    ret = lambda_handler(event, context)

    assert ret["statusCode"] == expected_output
