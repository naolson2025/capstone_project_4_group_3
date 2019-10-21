from django.shortcuts import render
from .models import Weather
from .weatherAPI import sort_data
import requests

# Create your views here.

def weather_list(request):
    # These two lines will get the weather data from the database
    #weather = Weather.objects.all()
    #return render(request, 'party_templates/home.html', {'weather': weather})

    weather_results = {}

    day_1 = {}
    day_2 = []
    day_3 = []
    day_4 = []
    day_5 = []

    if 'city' and 'country_code' in request.GET:
        city = request.GET['city']
        country_code = request.GET['country_code']
        # Create a query based on the inputs given from the user
        query = {'q': f'{city},{country_code}', 'units': 'imperial', 'appid': 'f08dea024433103844dc3ee09f370434'}

        url = f'https://api.openweathermap.org/data/2.5/forecast'
        # request data from the API server by combining the URL and query
        data = requests.get(url, params=query).json()
        weather_results = data['list']

        # call the sort data method from weatherAPI.py in order to format the data
        day_1, day_2, day_3, day_4, day_5 = sort_data(weather_results)
 
    #return render(request, 'party_templates/home.html', {'weather_results': weather_results}, {'day_1': day_1})
    return render(request, 'party_templates/home.html', {'day_1': day_1, 'day_2': day_2, 'day_3': day_3, 'day_4': day_4, 'day_5': day_5})