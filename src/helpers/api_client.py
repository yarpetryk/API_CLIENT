import requests
from requests import Response
from requests.auth import HTTPBasicAuth
from jsonschema import validate
from src.helpers.api_config import ApiConfig

api_config = ApiConfig()

class ApiClientBasicAuth:
    def __init__(self):
        self.api_config = ApiConfig()
        self.base_url = self.api_config.get_api_config().get("base_url")
        self.auth = HTTPBasicAuth(self.api_config.get_api_config().get("login"),
                                  self.api_config.get_api_config().get("password"))

    def send_get_request(self, path: str, schema: str) -> Response:
        request_path = self.base_url + path
        response = requests.get(request_path, auth=self.auth)
        validate(instance=response.json(), schema=schema)
        return response

    def send_post_request(self, path: str, body: str, schema: str) -> Response:
        request_path = self.base_url + path
        response = requests.post(request_path, auth=self.auth, json=body)
        validate(instance=response.json(), schema=schema)
        return response