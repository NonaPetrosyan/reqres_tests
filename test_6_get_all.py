import requests
import pytest
import allure


@pytest.mark.regression
@allure.feature('Reqres Feature')
@allure.suite('Get Tests')
@allure.title('Get All Users')
@allure.description('Test the GET endpoint to retrieve users from page 2 and verify the structure and content of the response.')
@allure.severity(allure.severity_level.NORMAL)
def test_get_reqres_users():
    with allure.step('Send GET request to retrieve users from page 2'):
        response = requests.get('https://reqres.in/api/users?page=2')

    with allure.step('Verify status code is 200'):
        assert response.status_code == 200, f'Expected status code 200, got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response contains "page" key'):
        assert 'page' in response_data, 'Response does not contain key "page"'

    with allure.step('Verify response contains "per_page" key'):
        assert 'per_page' in response_data, 'Response does not contain key "per_page"'

    with allure.step('Verify response contains "total" key'):
        assert 'total' in response_data, 'Response does not contain key "total"'

    with allure.step('Verify response contains "total_pages" key'):
        assert 'total_pages' in response_data, 'Response does not contain key "total_pages"'

    with allure.step('Verify response contains "data" key'):
        assert 'data' in response_data, 'Response does not contain key "data"'

    with allure.step('Verify "data" is a list'):
        assert isinstance(response_data['data'], list), '"data" should be a list'

    for user in response_data['data']:
        with allure.step('Verify user contains "id" key'):
            assert 'id' in user, 'User data does not contain key "id"'

        with allure.step('Verify user contains "email" key'):
            assert 'email' in user, 'User data does not contain key "email"'

        with allure.step('Verify user contains "first_name" key'):
            assert 'first_name' in user, 'User data does not contain key "first_name"'

        with allure.step('Verify user contains "last_name" key'):
            assert 'last_name' in user, 'User data does not contain key "last_name"'

        with allure.step('Verify user contains "avatar" key'):
            assert 'avatar' in user, 'User data does not contain key "avatar"'

    with allure.step('Verify response contains "support" key'):
        assert 'support' in response_data, 'Response does not contain key "support"'

    with allure.step('Verify support data contains "url" key'):
        assert 'url' in response_data['support'], 'Support data does not contain key "url"'

    with allure.step('Verify support data contains "text" key'):
        assert 'text' in response_data['support'], 'Support data does not contain key "text"'
