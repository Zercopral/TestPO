from http_requests.base_requests import base_request
from models.models import Order

class Store():

    # post
    def post_order(self, order_data: Order, expected_error=False):
        return base_request.post("store", "order", body=order_data.model_dump(by_alias=True), expected_error=expected_error)


    # get 1
    def get_order(self, store_order_id, expected_error=False):
        return base_request.get("store/order", store_order_id, expected_error=expected_error)


    # get 2
    def get_invetory(self, expected_error=False):
        return base_request.get("store", "inventory", expected_error=expected_error)
    

    # delete
    def delete_order(self, store_order_id: int = None, expected_error=False):
        return base_request.delete("store/order", store_order_id, expected_error=expected_error)
        
        
class User():

    # get
    def get_user(self, expected_error=False):
        return base_request.get("user", "login", expected_error=expected_error)
        

    # post
    def create(self, user_info, expected_error=False):
        return base_request.post("user", "", user_info, expected_error=expected_error)

    # put
    def update(self, user_name, update_user_info, expected_error=False):
        return base_request.put("user", user_name, update_user_info, expected_error=expected_error)


    # delete
    def delete(self, user_name, expected_error=False):
        return base_request.delete("user", user_name, expected_error=expected_error)