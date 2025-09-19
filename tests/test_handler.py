import pytest

from SGS.handler import lambda_handler

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
