import requests
import json

class Weather:

    base_url = 'http://api.weatherbit.io/v2.0'
    api_key = '0a59ad53609f462d909d03598f7f324f'

    def __init__(self, city):
        self.city = city

    def current(self):
        current_url = f'{Weather.base_url}/current'
        current_params = {
            'key': Weather.api_key,
            'lang': 'en',
            'units': 'M',
            'city': self.city
        }

        try:
            # Making a GET request
            response = requests.get(current_url, params=current_params)

            # Raise an exception for non-200 status codes
            response.raise_for_status()

            # Request was successful, handle the response data
            #print(response.json())

            response_data = json.loads(response.text)
            return response_data

        except requests.exceptions.RequestException as e:
            # Request failed, handle the error
            # print("Error:", e)
            return f'Error: {e}'


