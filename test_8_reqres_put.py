import requests
import pytest
import allure


@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('Reqres Feature')
@allure.suite('Update Tests')
@allure.title('Update User')
@allure.description('Test the PUT endpoint to update user information and verify the update with correct response fields.')
@allure.severity(allure.severity_level.CRITICAL)
def test_update_reqres_user():
    data = {
        "name": "morpheus",
        "job": "zion resident"
    }

    with allure.step('Send PUT request to update user information'):
        response = requests.put(
            'https://reqres.in/api/users/2',
            json=data
        )

    with allure.step('Verify status code is 200'):
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

    response_data = response.json()

    with allure.step('Verify response contains "name"'):
        assert 'name' in response_data, "Response does not contain 'name'"

    with allure.step('Verify the name in the response'):
        assert response_data['name'] == data['name'], f"Expected name to be '{data['name']}' but got '{response_data['name']}'"

    with allure.step('Verify response contains "job"'):
        assert 'job' in response_data, "Response does not contain 'job'"

    with allure.step('Verify the job in the response'):
        assert response_data['job'] == data['job'], f"Expected job to be '{data['job']}' but got '{response_data['job']}'"

    with allure.step('Verify response contains "updatedAt"'):
        assert 'updatedAt' in response_data, "Response does not contain 'updatedAt'"
