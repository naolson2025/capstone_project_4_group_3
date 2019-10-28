from django.shortcuts import render, redirect
from .models import Weather, RecipeSearch
from .weatherAPI import call_weather_api, sort_data
from .drinkAPI import call_drink_api
from .foodAPI import call_food_api, clean_food_data
import requests
from .forms import NewSearch

# Create your views here.

# Render the search.html template when the url is ''
def get_party_data(request):
    if request.method == 'POST':
        form = NewSearch(request.POST)
        user_search = form.save()
        if form.is_valid():
            user_search.save()
            return redirect('display_party_data')

    new_user_search_form = NewSearch()

    return render(request, 'party_templates/search.html', {'new_user_search_form': new_user_search_form})


def display_party_data(request):
    # Set blank variables for default render

    #drink_name = []
    #drink_ingredients = []
    #measurements = []

    #recipe_url = []
    #food_ingredients = []
    #food_name = []

    # Call the weather api from weatherAPI.py
    weather_data = call_weather_api()
    # call the sort data method from weatherAPI.py in order to format the data
    five_forecast_dates, average_temps = sort_data(weather_data)

    # Call the random drink api to provide a random drink recipe
    drink_name, drink_ingredients, measurements = call_drink_api()
    #drink_name = call_drink_api()

    # Get the most recent food type input from the user
    # Found .latest on stack overflow
    food = RecipeSearch.objects.latest('id')
    # Call the food api and provide the user's food type
    # returns a recipe for that food type
    recipe_url, food_ingredients, food_name = call_food_api(food)


    return render(request, 'party_templates/results.html', \
        {'five_forecast_dates': five_forecast_dates, 'average_temps': average_temps, \
        'drink_name': drink_name, 'drink_ingredients': drink_ingredients, 'measurements': measurements,\
        'recipe_url': recipe_url, 'food_ingredients': food_ingredients, 'food_name': food_name})

