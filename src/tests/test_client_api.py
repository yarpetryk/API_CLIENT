import pytest

from src.helpers.api_client import ApiClientBasicAuth
from src.schemas.devices import DevicesSchema
from src.schemas.current_data import CurrentDataSchema
from src.models.devices import DevicesModel


class TestApiDevices:
    api_client = ApiClientBasicAuth()
    devices_valid_schema = DevicesSchema.valid_schema_devices
    current_data_valid_schema = CurrentDataSchema.valid_schema_current_data
    current_data_model = DevicesModel.current_data_model()

    @pytest.mark.smoke
    def test_api_devices_list(self):
        """Tests the devices list with positive scenario"""
        response = self.api_client.send_get_request(path="/devices",
                                                    schema=self.devices_valid_schema)
        # Assert response status code
        assert response.status_code == 200
        # Assert response body
        for el in response.json():
            assert el['division'] == 0

    @pytest.mark.smoke
    def test_api_current_data(self):
        """Tests the current data with positive scenario"""
        response = self.api_client.send_post_request(path="/current/0/operating",
                                                     body=self.current_data_model,
                                                     schema=self.current_data_valid_schema)
        # Assert response status code
        assert response.status_code == 200
        # Assert response body
        assert response.json()['watt'] == 0
