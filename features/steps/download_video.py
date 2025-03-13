import requests
import json
from behave import given, when, then

BASE_URL = "http://127.0.0.1:8000"


@given('the user sends a PUT request to "{endpoint}" with body')
def step_send_put_request(context, endpoint):
    body = json.loads(context.text)
    context.response = requests.put(BASE_URL + endpoint, json=body)

@then("the response code should be {status_code:d}")
def step_check_status_code(context, status_code):
    assert context.response.status_code == status_code, f"Expected {status_code}, got {context.response.status_code}"
