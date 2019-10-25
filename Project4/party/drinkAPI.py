import requests
import os

def call_drink_api():

    url = "https://the-cocktail-db.p.rapidapi.com/random.php"

    headers = {
    'x-rapidapi-host': "the-cocktail-db.p.rapidapi.com",
    'x-rapidapi-key': "611386d4a7mshdfb5beebe926ae1p127f3ejsn1014e979f01a"
    }

    random_drink = requests.request("GET", url, headers=headers).json()

    return random_drink['list']

def filter_drink_api(random_drink):

    for drink in random_drink:
        drink_name = drink['strDrink']
        drink_catagory = drink['strCatagory']

        print(f'Drink name is: {drink_name} Drink catagory is: {drink_catagory} ')

        


