import requests
import pytest
import allure

@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('Reqres Feature')
@allure.suite('Login Tests')
@allure.title('Successful Login')
@allure.description('Test the login endpoint with valid credentials and verify successful login.')
@allure.severity(allure.severity_level.CRITICAL)
def test_reqres_successful_login():

    data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    with allure.step('Send POST request for successful login'):
        response = requests.post(
            'https://reqres.in/api/login',
            json=data,
        )

    with allure.step('Verify status code is 200'):
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

    response_data = response.json()

    with allure.step('Verify response contains "token" field'):
        assert 'token' in response_data, 'Response should contain a "token" field'

    with allure.step('Verify "token" is a non-empty string'):
        assert isinstance(response_data['token'], str) and response_data['token'], '"token" should be a non-empty string'
