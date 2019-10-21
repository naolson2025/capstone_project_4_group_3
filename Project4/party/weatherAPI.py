import requests
import os
from datetime import datetime
# My code is using the time provided by the API
def main():
    print('Get the 5 day weather forecast for any city.')
    # An environment key must be set for the program to work
    #key = os.environ.get('WEATHER_KEY')
    # Loop if a user enters invalid city or country
    while True:
        try:
            print("Type 'break' to end.")
            city = input('Enter a city name: ')
            if city.lower() != 'break':
                country_code = input('Enter the country code: ')
                # Create a query based on the inputs given from the user
                query = {'q': f'{city},{country_code}', 'units': 'imperial', 'appid': f08dea024433103844dc3ee09f370434}

                url = f'https://api.openweathermap.org/data/2.5/forecast'
                # request data from the API server by combining the URL and query
                data = requests.get(url, params=query).json()
                forecast = data['list']
                # Send the API info trimmed to just the 'list' to the sort_data function
                sort_data(forecast)
                break
            else:
                break
        except:
            print('The city or country code you entered was invalid.')


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

    day_1_formatted = []
    day_2_formatted = []
    day_3_formatted = []
    day_4_formatted = []
    day_5_formatted = []

    # Display the 5 day lists with the 3 hour intervals
    print()
    print('{:25} {:11} {:20} {:15}'.format('Date and Time', 'Temp', 'Weather', 'Wind Speed'))
    for day in day_1:
        print('{:25} {:1} {:5} {:20} {:15}'.format(day['dt_txt'], str(day['main']['temp']), 'F', day['weather'][0]['description'], str(day['wind']['speed'])))
        #formatted_forecast_1 = '{:25} {:1} {:5} {:20} {:15}'.format(day['dt_txt'], str(day['main']['temp']), 'F', day['weather'][0]['description'], str(day['wind']['speed']))
        formatted_forecast_1 = '{} {}F {}'.format(day['dt_txt'], str(day['main']['temp']), day['weather'][0]['description'])
        day_1_formatted.append(formatted_forecast_1)

    print()
    for day in day_2:
        print('{:25} {:1} {:5} {:20} {:15}'.format(day['dt_txt'], str(day['main']['temp']), 'F', day['weather'][0]['description'], str(day['wind']['speed'])))
        formatted_forecast_2 = '{} {}F {}'.format(day['dt_txt'], str(day['main']['temp']), day['weather'][0]['description'])
        day_2_formatted.append(formatted_forecast_2)

    print()
    for day in day_3:
        print('{:25} {:1} {:5} {:20} {:15}'.format(day['dt_txt'], str(day['main']['temp']), 'F', day['weather'][0]['description'], str(day['wind']['speed'])))
        formatted_forecast_3 = '{} {}F {}'.format(day['dt_txt'], str(day['main']['temp']), day['weather'][0]['description'])
        day_3_formatted.append(formatted_forecast_3)

    print()
    for day in day_4:
        print('{:25} {:1} {:5} {:20} {:15}'.format(day['dt_txt'], str(day['main']['temp']), 'F', day['weather'][0]['description'], str(day['wind']['speed'])))
        formatted_forecast_4 = '{} {}F {}'.format(day['dt_txt'], str(day['main']['temp']), day['weather'][0]['description'])
        day_4_formatted.append(formatted_forecast_4)

    print()
    for day in day_5:
        print('{:25} {:1} {:5} {:20} {:15}'.format(day['dt_txt'], str(day['main']['temp']), 'F', day['weather'][0]['description'], str(day['wind']['speed'])))
        formatted_forecast_5 = '{} {}F {}'.format(day['dt_txt'], str(day['main']['temp']), day['weather'][0]['description'])
        day_5_formatted.append(formatted_forecast_5)

    return day_1_formatted, day_2_formatted, day_3_formatted, day_4_formatted, day_5_formatted


if __name__ == '__main__':
    main()