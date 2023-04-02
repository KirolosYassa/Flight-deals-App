from data_manager import *
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    
    def __init__(self, locations=["Paris", "Berlin"], date_from="01/04/2023", date_to="31/05/2023"):
        self.date_from = date_from
        self.date_to = date_to
        self.locations = locations
        self.KIWI_API_KEY = os.getenv("KIWI_API_KEY")
        self.KIWI_URL = "https://api.tequila.kiwi.com"
        self.kiwi_headers ={
            "Content-Type": "application/json",
            "Content-Encoding": "gzip",
            "apikey": self.KIWI_API_KEY,
        }
        
    
    def get_prices_by_iataCodes(self, sheet):
        prices_of_each_city = []
        for city in sheet["prices"]:
            url = f"{self.KIWI_URL}/search"     

            tomorrow = datetime.now() + timedelta(days=1)
            six_months_from_tomorrow = datetime.now() + timedelta(days=180)
            tomorrow = datetime.strftime(tomorrow, "%d/%m/%Y")
            six_months_from_tomorrow = datetime.strftime(six_months_from_tomorrow, "%d/%m/%Y")
            print(tomorrow, six_months_from_tomorrow)
            
            self.kiwi_parameters = {
                "fly_from": "EG",
                "fly_to": "PAR",
                "date_from": tomorrow,
                "date_to": six_months_from_tomorrow,
                "price_to": city["lowestPrice"],
            }
            response = requests.get(url=url, params=self.kiwi_parameters, headers=self.kiwi_headers)
            data = response.json()
            # print(response)
            if data:
                result = data["data"]
                price = result["price"][0]
                print(price)
            else:
                print("No results found.")

            # print(result["data"][0])
            # prices_of_each_city.append({
            #     "iataCode": city["iataCode"],
            #     "price": result["data"][0]["price"],
            # })
        return prices_of_each_city
        
    
    def get_iata_code_field(self, city):   
        url = f"{self.KIWI_URL}/locations/query"     
        self.kiwi_parameters = {
            "term": city,
        }
        response = requests.get(url=url, params=self.kiwi_parameters, headers=self.kiwi_headers)
        result = response.json()
        # print(response)
        # print(result)
        return result["locations"][0]["code"]


# flightsearch = FlightSearch()
# print(flightsearch.get_prices_by_iataCodes())
# # ["locations"]["alternative_departure_points"]["id"]

