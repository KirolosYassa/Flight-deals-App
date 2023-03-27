from data_manager import *
import requests
from datetime import datetime
from dotenv import load_dotenv
import os
load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    
    def __init__(self, locations=["PRG", "ITS"], date_from="01/04/2023", date_to="31/05/2023"):
        self.date_from = date_from
        self.date_to = date_to
        self.locations = locations
        self.KIWI_API_KEY = os.getenv("KIWI_API_KEY")
        self.KIWI_URL = "https://api.tequila.kiwi.com/v2"
        self.kiwi_headers ={
            "Content-Type": "application/json",
            "Content-Encoding": "gzip",
        }
        
        self.search_for_flight()
    
    def search_for_flight(self):
        for city in self.locations:
            
            self.kiwi_parameters = {
                        "apikey": self.KIWI_API_KEY,
                        "adults": 1,
                        # "locations": locations,
                        "nights_range": [3,  5],
                        "date_from":self.date_from,
                        "date_to":self.date_to,
                        "fly_from": "EGYPT",
                        "fly_from": city,
                        }
            response = requests.post(url=self.KIWI_URL, params=self.kiwi_parameters, headers=self.kiwi_headers)
            result = response.json()
            print(response)
            print(result)



# dataManager = DataManager()
# dataManager.get_sheet_rows()

flightsearch = FlightSearch()
