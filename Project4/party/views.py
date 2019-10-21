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
    print(request)
    print(request.GET)
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
        return render(request, 'party_templates/home.html', {'day_1': day_1, 'day_2': day_2, 'day_3': day_3, 'day_4': day_4, 'day_5': day_5})
    elif 'random-drink' in request.GET:
        random_drink = drink_list(request)
        return render(request, 'party_templates/home.html', {'random_drink': random_drink}) 
    #return render(request, 'party_templates/home.html', {'weather_results': weather_results}, {'day_1': day_1})



def drink_list(request):
    random_drink = {}
    print('made it here')
    if 'random-drink' in request.GET:
    #if request.method == 'GET':

        url = "https://the-cocktail-db.p.rapidapi.com/random.php"

        headers = {
        'x-rapidapi-host': "the-cocktail-db.p.rapidapi.com",
        'x-rapidapi-key': "611386d4a7mshdfb5beebe926ae1p127f3ejsn1014e979f01a"
        }

        #query = {'x-rapidapi-host': "the-cocktail-db.p.rapidapi.com", 'x-rapidapi-key': "611386d4a7mshdfb5beebe926ae1p127f3ejsn1014e979f01a"}
        random_drink = requests.request("GET", url, headers=headers).json()
        #random_drink = requests.get(url, params=query)
        print(random_drink)

    print()
    print(random_drink)
    #return render(request, 'party_templates/home.html', {'random_drink': random_drink})    
    return random_drink