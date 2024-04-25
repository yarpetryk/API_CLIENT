import requests
from requests import Response
from requests.auth import HTTPBasicAuth
from jsonschema import validate
from src.helpers.api_config import ApiConfig

api_config = ApiConfig()

class ApiClientBasicAuth:
    BASE_URL = api_config.get_api_config().get("base_url")
    AUTH = HTTPBasicAuth(api_config.get_api_config().get("login"),
                            api_config.get_api_config().get("password"))


    def send_get_request(self, path: str, schema: str) -> Response:
        request_path = self.BASE_URL + path
        response = requests.get(request_path, auth=self.AUTH)
        validate(instance=response.json(), schema=schema)
        return response

    def send_post_request(self, path: str, body: str, schema: str) -> Response:
        request_path = self.BASE_URL + path
        response = requests.post(request_path, auth=self.AUTH, json=body)
        validate(instance=response.json(), schema=schema)
        return response