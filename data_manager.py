import json
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
            "Authorization": f"Bearer {self.TOKEN}",
            "Content-Type": "application/json",
    #         "Content-Encoding": "gzip",

        }
        # print(self.ENDPOINT_SHEETY)
        self.sheet = self.get_sheet_data()
        
    def get_sheet_data(self):
        response = requests.get(url=self.ENDPOINT_SHEETY, headers=self.bearer_headers)
        result = response.json()
        # print(response)
        # print(result)
        return result
    
    def update_sheet_data(self, sheetdata):
        # print(f"sheetdata at data manager = {sheetdata}")
        try:
            for row in sheetdata:
                # print(row)
                url = self.ENDPOINT_SHEETY + "/" + str(row["id"])
                # print(url)
                row_data = {
                    "price":{
                            'city': row["city"],
                            'iataCode': row["iataCode"],
                            'lowestPrice': row["lowestPrice"],
                            'id': row["id"],
                            }
                }
                response = requests.put(url=url, json = row_data, headers=self.bearer_headers)
                result = response.json()
                # print(response.status_code)
                # print(result)
            return True
        except Exception as e:
            print(e.message)
            return False
        
            
# dataManager = DataManager()
# dataManager.get_sheet_data()
