import requests
import pytest
import allure

my_id = None


@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('Reqres Feature')
@allure.suite('User Creation Tests')
@allure.title('Successful User Creation')
@allure.description('Test the user creation endpoint with valid data and verify successful creation.')
@allure.severity(allure.severity_level.CRITICAL)
def test_reqres_successful_user_creation():

    data = {
        "name": "morpheus",
        "job": "leader"
    }

    with allure.step('Send POST request for user creation'):
        response = requests.post(
            'https://reqres.in/api/users',
            json=data,
        )

    with allure.step('Verify status code is 201'):
        assert response.status_code == 201, f"Expected status code 201 but got {response.status_code}"

    response_data = response.json()

    with allure.step('Verify response contains "name" field'):
        assert 'name' in response_data, 'Response should contain a "name" field'
        assert response_data['name'] == data['name'], 'The "name" field value does not match the request data'

    with allure.step('Verify response contains "job" field'):
        assert 'job' in response_data, 'Response should contain a "job" field'
        assert response_data['job'] == data['job'], 'The "job" field value does not match the request data'

    with allure.step('Verify response contains "id" field'):
        assert 'id' in response_data, 'Response should contain an "id" field'

    with allure.step('Verify response contains "createdAt" field'):
        assert 'createdAt' in response_data, 'Response should contain a "createdAt" field'

    with allure.step('Store created user ID'):
        global my_id
        my_id = response_data['id']
        print(f"Created user ID: {my_id}")
