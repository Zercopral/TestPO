from http_requests.api_requests import (Store, User)
from models.models import Order, WrongOrder, DefaultUser
from utils.schema import validate_schema

import allure
import pytest

@allure.feature('Swagger API Test')
@allure.story('Petstore API')
class TestAPI:
        @allure.title('correct_http_code_correct_data')
        def test_correct_http_code_correct_data(self):
                payload = Order()
                response = Store().post_order(payload)

                assert response.status_code == 200


        @allure.title('correct_data_successful_request')
        def test_correct_data_successful_request(self):
                payload = Order()
                response = Store().post_order(payload)

                assert validate_schema(response.json(), Order.model_json_schema()) == True


        @allure.title('correct_http_code_incorrect_data')
        def test_correct_http_code_incorrect_data(self):
                payload = WrongOrder()
                response = Store().post_order(payload, expected_error=True)

                assert response.status_code == 500

        
        @allure.title('correct_data_incorrect_request')
        def test_correct_data_incorrect_request(self):
                payload = WrongOrder()
                response = Store().post_order(payload, expected_error=True)

                assert response.json().get('message', '') == "something bad happened"


        @allure.title('correct_data_unacceptable_request')
        def test_correct_http_code_unacceptable_data(self):
                payload = DefaultUser()
                response = Store().post_order(payload, expected_error=True)

                assert response.status_code != 200