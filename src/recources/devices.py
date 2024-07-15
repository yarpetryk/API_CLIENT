from src.helpers.api_client import ApiClientBasicAuth


class Devices:
    api_client = ApiClientBasicAuth()

    def get_devices_list(self, schema: str):
        response = self.api_client.send_get_request(path="/devices", schema=schema)
        if response is not None:
            return response.json()
        return None

    def get_current_data(self, body: str, schema: str):
        response = self.api_client.send_post_request(path="/current/0/operating", body=body, schema=schema)
        if response is not None:
            return response.json()
        return None
