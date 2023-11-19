from http_requests.api_requests import (Store, User)
from models.models import Order, DefaultUser, UpdateUser
from utils.schema import validate_schema

import allure
import pytest

@allure.feature('Swagger Petstore')
@allure.story('Petstore API')
class TestAPI:
        @allure.title('store_post_order')
        def test_store_post_order(self):
                payload = Order()
                response = Store().post_order(payload)

                json_response = response.json()

                assert response.status_code == 200

                validate_schema(json_response, Order.model_json_schema())


        # store_api: Store
# data1 = Order().model_dump(by_alias=True)

# store_order_info = base_request.get("store/order", store_order_id)

# delete_order_message = base_request.get(
#             "store/order", delete_order_id, expected_error=True
#         )
#         pprint.pprint(delete_order_message)