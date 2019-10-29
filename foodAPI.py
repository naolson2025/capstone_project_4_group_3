
import requests
import os
from  requests.exceptions import HTTPError

URL = url = "https://api.edamam.com/search"

class call_food_api():

 def search_food(self,search_term):

    key = os.environ.get('MY_KEY')
    # set up parameters for the api query q=keywords, c=category and set to food_type to enforce that we
    # are  always searching for food type
    parameters = {'q': {search_term},'c': 'meal_type', 'app_id': '273626ba','app_key': {key}}

    # request data from edaman.com
    try:
        response = requests.get(URL,params=parameters)

        # Only raises error if certain response codes are returned
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error: {http_err}')
    except Exception as ex:
        print(f'other error: {ex}')
    else:
        return response


