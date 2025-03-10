import requests
from behave import given, when, then


@given("the server is up and running correctly")
def step_server_is_running(context):
  pass

@when('a GET request is sent to "{endpoint}"')
def step_send_get_request(context, endpoint):
    context.response = requests.get("http://127.0.0.1:8000" + endpoint)

@then("the response code should be {status_code:d}")
def step_check_status_code(context, status_code):
    assert context.response.status_code == status_code, f"Expected {status_code}, got {context.response.status_code}"
