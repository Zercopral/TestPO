from http_requests.base_requests import base_request
from models.models import Order, DefaultUser, UpdateUser

class Store():

    # post
    def post_order(self, order_data: Order):
        return base_request.post("store", "order", body=order_data.model_dump(by_alias=True))


    # get 1
    def get_order(self, store_order_id):
        return base_request.get("store/order", store_order_id)


    # get 2
    def get_invetory(self):
        return base_request.get("store", "inventory")
    

    # delete
    def delete_order(self, store_order_id: int = None):
        return base_request.delete("store/order", store_order_id)
        
        
class User():

    # get
    def get_user(self):
        return base_request.get("user", "login")
        

    # post
    def create(self, user_info):
        return base_request.post("user", "", user_info)

    # put
    def update(self, user_name, update_user_info):
        return base_request.put("user", user_name, update_user_info)


    # delete
    def delete(self, user_name):
        return base_request.delete("user", user_name)