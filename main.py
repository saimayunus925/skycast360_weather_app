# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests, sqlite3 # "requests": used to make HTTP requests/responses with API endpoints
# "sqlite3": used to write SQL queries to a SQLite DB with Python
import os # we need the os library's getenv() function to get our API key from our .env file

def api_response(api_endpoint: str, parameters: list):
    # reads in an API endpoint, returns the endpoint's HTTP response data in JSON format
    # api_endpoint: the API endpoint URL we're getting data from
    # parameters: the parameters/options we need for the endpoint so we can get the specific data we need
    pass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    api_key = os.getenv("WEATHER_API_KEY") # our weather API key
    # step 1: read in the city whose weather we need
    city = input("City: ") # city (e.g. San Francisco)
    # we'll figure out state and country stuff later: states are for US only, countries need ISO 3166 codes
    # step 2: get latitude/longitude of the city with OpenWeather's Geocoding API, OpenWeather's weather data API endpoint needs those
    latitude_longitude_endpoint = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api_key}"
    latitude_longitude_response = requests.get(latitude_longitude_endpoint) # response data for the given city, has the city's latitude/longitude coordinates
    print(latitude_longitude_response.json())
    # step 3: query the API with the city/state/country/latitude/longitude info
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
