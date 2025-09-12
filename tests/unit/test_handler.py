import json

import pytest

from SGS.SGS import app

def test_lambda_handler():

    event = {"test": "test"}
    context = None
    ret = app.lambda_handler(event, context)

    assert ret["statusCode"] == 200

