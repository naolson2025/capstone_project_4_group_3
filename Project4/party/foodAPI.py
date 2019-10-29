import requests
import os

def call_food_api(food_type):
    # static url for calling the api
    url = "https://api.edamam.com/search"
    # query that is appended to the url depending on the users entry
    query = {'q': f'{food_type}', 'app_id': '273626ba','app_key': '8021d138cdb76ecc66e90c1b3fbb5f38', 'from': 0, 'to': 1}
    # return the json response from the api server
    data = requests.get(url, params=query).json()
    url, ingredients, food_name = clean_food_data(data)
    
    return url, ingredients, food_name


def clean_food_data(data):
    
    url = data['hits'][0]['recipe']['shareAs']
    ingredients = data['hits'][0]['recipe']['ingredientLines']
    food_name = data['hits'][0]['recipe']['label']

    return url, ingredients, food_name