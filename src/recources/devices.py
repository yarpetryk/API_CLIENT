from src.helpers.api_client import ApiClientBasicAuth


class Devices:
    api_client = ApiClientBasicAuth()

    def get_devices_list(self, schema: str):
        return self.api_client.send_get_request(path="/devices", schema=schema)

    def get_current_data(self, body: str, schema: str):
        return self.api_client.send_post_request(path="/current/0/operating", body=body, schema=schema)
