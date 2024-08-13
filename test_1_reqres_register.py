import requests
import pytest
import allure


@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('Reqres Feature')
@allure.suite('Registration Tests')
@allure.title('Successful Registration')
@allure.description('Test the registration endpoint with valid credentials and verify successful registration.')
@allure.severity(allure.severity_level.CRITICAL)
def test_reqres_successful_registration():
    data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    with allure.step('Send POST request for successful registration'):
        response = requests.post(
            'https://reqres.in/api/register',
            json=data,
        )

    with allure.step('Verify status code is 200'):
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

    response_data = response.json()

    with allure.step('Verify response contains "id" field'):
        assert 'id' in response_data, 'Response should contain an "id" field'

    with allure.step('Verify "id" is an integer'):
        assert isinstance(response_data['id'], int), '"id" should be an integer'

    with allure.step('Verify response contains "token" field'):
        assert 'token' in response_data, 'Response should contain a "token" field'

