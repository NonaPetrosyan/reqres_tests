import requests
import pytest
import allure


@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('Reqres Feature')
@allure.suite('Registration Tests')
@allure.title('Unsuccessful Registration')
@allure.description(
    'Test the registration endpoint with missing password and verify the appropriate error message is returned.')
@allure.severity(allure.severity_level.CRITICAL)
def test_reqres_unsuccessful_registration():
    data = {
        "email": "eve.holt@reqres.in"
    }

    with allure.step('Send POST request for unsuccessful registration'):
        response = requests.post(
            'https://reqres.in/api/register',
            json=data,
        )

    with allure.step('Verify status code is 400'):
        assert response.status_code == 400, f"Expected status code 400 but got {response.status_code}"

    response_data = response.json()

    with allure.step('Verify response contains "error" field'):
        assert 'error' in response_data, "Response does not contain 'error'"

    with allure.step('Verify error message is "Missing password"'):
        assert response_data['error'] == "Missing password", "Error message does not match"
