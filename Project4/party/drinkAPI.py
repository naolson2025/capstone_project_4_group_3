import requests
import os

def drink_API():
    print('Drinks for the Occasion')

    #Temp key, not sure how to save into directory on a mac yet
    key = "1"

    while True: 

        try:
            drink_name = str(input("Enter the name of drink you want: "))

            query = {"i" : drink_name}

            url= f"https://the-cocktail-db.p.rapidapi.com/search.php"

        except: 
            print("The drink name was invalid, try again. ")


