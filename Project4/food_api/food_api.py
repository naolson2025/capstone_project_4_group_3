import requests    # Importing the  request library
import os           # Importing the OS


def main():

    key = os.environ.get('MY_KEY')

    name = get_name()
    brand_name =get_brand_name()
    calories = get_calories()
    display_menu( name,brand_name, calories)

def get_name():
    name = input('Enter name:  ' )
    return name

def get_brand_name():
    brand_name = input('Enter brand name: ')
    return brand_name

def get_calories():
    return float(input('Enter calories: '))

def request_menu(name):
    url ={' https://api.nutritionix.com/v1_1/search/mcdonalds?results=0:20&fields=item_name,brand_name,item_id,nf_calories&appId=9f8de9e6&appKey=ab5f574c34404ea6764812d31c868687':name}

    # Defining a params dict for the parameters to be sent to the API
    params = {'q': 'item_name','brand_name': 'McDonal','nf_calories': '','nf_serving_size_unit': 'serving'}
    return params.get(url)

def display_menu(name,brand_name, calories):
    requests.get(' https://api.nutritionix.com/v1_1/search/mcdonalds?results=0:20&fields=item_name,brand_name,item_id,nf_calories&appId=9f8de9e6&appKey=ab5f574c34404ea6764812d31c868687').json()



    print(f'The food item is {name}, the brand name is {brand_name} and the calories content is {calories}')


if __name__ == '__main__':
    main()