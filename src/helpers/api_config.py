import os
from dotenv import load_dotenv


class ApiConfig:

    PATH = "./config.env"

    def get_api_config(self):
        load_dotenv(dotenv_path=self.PATH)
        return {
            "login": os.getenv("LOGIN"),
            "password": os.getenv("PASSWORD"),
            "base_url": os.getenv("BASE_URL")
        }
