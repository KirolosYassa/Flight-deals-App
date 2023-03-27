import requests
from dotenv import load_dotenv
import os
load_dotenv()


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.TOKEN = os.getenv("TOKEN")
        self.ENDPOINT_SHEETY = os.getenv("ENDPOINT_SHEETY")
        self.bearer_headers = {
            "Authorization": f"Bearer {self.TOKEN}"
        }
        print(self.ENDPOINT_SHEETY)
        
        
    def get_sheet_rows(self):
        response = requests.get(url=self.ENDPOINT_SHEETY, headers=self.bearer_headers)
        result = response.json()
        print(response)
        print(result)
        return result
    

# dataManager = DataManager()
# dataManager.get_sheet_rows()