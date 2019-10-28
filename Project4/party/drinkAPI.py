import requests
import os

def call_drink_api():

    url = "https://the-cocktail-db.p.rapidapi.com/random.php"

    headers = {
    'x-rapidapi-host': "the-cocktail-db.p.rapidapi.com",
    'x-rapidapi-key': "611386d4a7mshdfb5beebe926ae1p127f3ejsn1014e979f01a"
    }

    random_drink = requests.request("GET", url, headers=headers).json()

    drink_name, ingredients, measurements = clean_drink_api(random_drink)
   
    return drink_name, ingredients, measurements


def clean_drink_api(data):
    # Pull the drink name from the data
    drink_name = data['drinks'][0]['strDrink']
    # We don't know how many ingredients there will be so we need to add them to this list
    ingredients = []

    # Each recipe has a different number of ingredients so to get them all I will loop through until the strIngredient# = None
    ingredient_counter = 1
    ingredient_string = 'strIngredient'
    while True:
        ingredient = data['drinks'][0][ingredient_string + str(ingredient_counter)]
        if ingredient != None:
            ingredients.append(ingredient)
            ingredient_counter += 1
            ingredient = data['drinks'][0][ingredient_string + str(ingredient_counter)]
        else:
            break


    # Not sure how many measurement there will be so I will need to add them to this empty list
    measurements = []
    # Each recipe has a different number of ingredients and each ingredient has a measurement so loop through to get all measurements
    measurement_counter = 1
    measurement_string = 'strMeasure'

    while True:
        measurement = data['drinks'][0][measurement_string + str(measurement_counter)]
        if measurement != None:
            measurements.append(measurement)
            measurement_counter += 1
            measurement = data['drinks'][0][measurement_string + str(measurement_counter)]
        else:
            break

    return drink_name, ingredients, measurements