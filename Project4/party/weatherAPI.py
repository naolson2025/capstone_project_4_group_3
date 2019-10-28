import requests
import os
from datetime import datetime


def call_weather_api():
    # An environment key must be set for the program to work
    #key = os.environ.get('WEATHER_KEY')
    # Create a query based on the inputs given from the user
    query = {'q': f'minneapolis,us', 'units': 'imperial', 'appid': 'f08dea024433103844dc3ee09f370434'}

    url = f'https://api.openweathermap.org/data/2.5/forecast'
    # request data from the API server by combining the URL and query
    data = requests.get(url, params=query).json()
    return data['list']

    

def sort_data(forecast):
    five_forecast_dates = []

    # Loop through all items that the API provided and find all unique dates. Since we know they provide 5 days there should be 5 uniqe dates in the list above
    for interval in forecast:
        # Found date formatting on stack overflow
        if datetime.strptime(interval['dt_txt'], '%Y-%m-%d %H:%M:%S').date() not in five_forecast_dates:
            five_forecast_dates.append(datetime.strptime(interval['dt_txt'], '%Y-%m-%d %H:%M:%S').date())

    # Create empty lists for the five unique dates
    day_1 = []
    day_2 = []
    day_3 = []
    day_4 = []
    day_5 = []

    # Loop through the API data to put all weather intervals for a given day into its list
    for interval in forecast:
        if datetime.strptime(interval['dt_txt'], '%Y-%m-%d %H:%M:%S').date() == five_forecast_dates[0]:
            day_1.append(interval)
        elif datetime.strptime(interval['dt_txt'], '%Y-%m-%d %H:%M:%S').date() == five_forecast_dates[1]:
            day_2.append(interval)
        elif datetime.strptime(interval['dt_txt'], '%Y-%m-%d %H:%M:%S').date() == five_forecast_dates[2]:
            day_3.append(interval)
        elif datetime.strptime(interval['dt_txt'], '%Y-%m-%d %H:%M:%S').date() == five_forecast_dates[3]:
            day_4.append(interval)
        elif datetime.strptime(interval['dt_txt'], '%Y-%m-%d %H:%M:%S').date() == five_forecast_dates[4]:
            day_5.append(interval)
        else:
            print('Error')
            print(interval)


    average_temps = []
    # Found round() on stack overflow
    number_of_days = 0
    day_1_total_temp = 0
    for day in day_1:
        day_1_total_temp += day['main']['temp']
        number_of_days += 1

    day_1_average_temp = day_1_total_temp / number_of_days
    average_temps.append(round(day_1_average_temp, 2))


    number_of_days = 0
    day_2_total_temp = 0
    for day in day_2:
        day_2_total_temp += day['main']['temp']
        number_of_days += 1
    day_2_average_temp = day_2_total_temp / number_of_days
    average_temps.append(round(day_2_average_temp, 2))


    number_of_days = 0
    day_3_total_temp = 0
    for day in day_3:
        day_3_total_temp += day['main']['temp']
        number_of_days += 1
    day_3_average_temp = day_3_total_temp / number_of_days
    average_temps.append(round(day_3_average_temp, 2))


    number_of_days = 0
    day_4_total_temp = 0
    for day in day_4:
        day_4_total_temp += day['main']['temp']
        number_of_days += 1
    day_4_average_temp = day_4_total_temp / number_of_days
    average_temps.append(round(day_4_average_temp, 2))


    number_of_days = 0
    day_5_total_temp = 0
    for day in day_5:
        day_5_total_temp += day['main']['temp']
        number_of_days += 1
    day_5_average_temp = day_5_total_temp / number_of_days
    average_temps.append(round(day_5_average_temp, 2))

    
    return five_forecast_dates, average_temps