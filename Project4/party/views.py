from django.shortcuts import render
from weatherAPI import call_weather_api, sort_data
from drinkAPI import call_drink_api
from foodAPI import call_food_api


# Create your views here.

def get_party_data(request):
    # Set blank variables for default render
    day_1 = []
    day_2 = []
    day_3 = []
    day_4 = []
    day_5 = []
    random_drink = []
    recipe = []


    if 'city' and 'country_code' in request.GET:
        city = request.GET['city']
        country_code = request.GET['country_code']

        weather_data = call_weather_api(city, country_code)
        # call the sort data method from weatherAPI.py in order to format the data
        day_1, day_2, day_3, day_4, day_5 = sort_data(weather_data)


    if 'random-drink' in request.GET:
        random_drink = call_drink_api()


    if 'food' in request.GET:
        food = request.GET['food']
        recipe = call_food_api(food)


    return render(request, 'party_templates/home.html', {'day_1': day_1, 'day_2': day_2, 'day_3': day_3, 'day_4': day_4, 'day_5': day_5, 'random_drink': random_drink, 'recipe': recipe})
