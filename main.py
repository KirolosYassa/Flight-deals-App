#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import *
from flight_search import *


dataManager = DataManager()
# sheetdata = dataManager.get_sheet_data() 
sheetdata = dataManager.sheet
print(sheetdata)
flightSearch = FlightSearch()

def add_iata_code_field(sheet_data, city):
    iata_code = flightSearch.get_iata_code_field(city)
    print(iata_code)
    return {'city': sheet_data["city"], 'iataCode': iata_code, 'lowestPrice': sheet_data["lowestPrice"], 'id': sheet_data["id"]}

new_sheet_data = [ add_iata_code_field(sheet, sheet["city"]) for sheet in sheetdata["prices"]  if sheet["iataCode"] == "" ]

print(new_sheet_data)

updating_google_sheet_status = dataManager.update_sheet_data(new_sheet_data)
print(updating_google_sheet_status)

sheetdata = dataManager.get_sheet_data()
print(sheetdata)
print(flightSearch.get_prices_by_iataCodes(sheetdata))

