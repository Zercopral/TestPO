import requests
import pprint
import json
from settings import BASE_URL_PETSTORE

# создать свои запросы для сущностей тестируемого API (по 4 запроса) user и store
# по базовому url с реализацией базового класса
# тестирования(пример приведен в репозитории)


class BaseRequest:
    def __init__(self, base_url):
        self.base_url = base_url
        # set headers, authorisation etc

    def _request(self, url, request_type, data=None, expected_error=False):
        stop_flag = False
        headers = {"content-type": "application/json", "api_key": "ithub_suks"}
        if data:
            data = json.dumps(data)
            print(data)

        while not stop_flag:
            if request_type == "GET":
                response = requests.get(url, headers=headers)
            elif request_type == "POST":
                response = requests.post(url, data=data, headers=headers)
            elif request_type == "PUT":
                response = requests.put(url, data=data, headers=headers)
            else:
                response = requests.delete(url, headers=headers)

            if not expected_error and response.status_code == 200:
                stop_flag = True
            elif expected_error:
                stop_flag = True

            pprint.pprint("Trying to connect..." + url)
            pprint.pprint(response.status_code)
            pprint.pprint(response.reason)

        pprint.pprint(f"{request_type} example")
        pprint.pprint(response.url)
        pprint.pprint(response.status_code)
        pprint.pprint(response.reason)
        pprint.pprint(response.text)
        pprint.pprint(response.json())
        pprint.pprint("**********")

        return response

    def get(self, endpoint, endpoint_id, expected_error=False):
        url = f"{self.base_url}/{endpoint}/{endpoint_id}"
        response = self._request(url, "GET", expected_error=expected_error)
        return response


    def post(self, endpoint, endpoint_id, body, expected_error=False):
        if endpoint_id == "":
            url = f"{self.base_url}/{endpoint}"
        else:
            url = f"{self.base_url}/{endpoint}/{endpoint_id}"
        response = self._request(url, "POST", data=body, expected_error=expected_error)
        return response


    def put(self, endpoint, endpoint_id, body, expected_error=False):
        url = f"{self.base_url}/{endpoint}/{endpoint_id}"
        response = self._request(url, "PUT", data=body, expected_error=expected_error)
        return response


    def delete(self, endpoint, endpoint_id, expected_error=False):
        url = f"{self.base_url}/{endpoint}/{endpoint_id}"
        response = self._request(url, "DELETE", expected_error=expected_error)
        return response


base_request = BaseRequest(BASE_URL_PETSTORE)