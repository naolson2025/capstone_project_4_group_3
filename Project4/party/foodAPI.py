import requests
import os

def call_food_api(food_type):
    # static url for calling the api
    url = "https://api.edamam.com/search"
    # query that is appended to the url depending on the users entry
    query = {'q': f'{food_type}', 'app_id': '273626ba','app_key': '8021d138cdb76ecc66e90c1b3fbb5f38'}
    # return the json response from the api server
    return requests.get(url, params=query).json()