from django.test import TestCase
import unittest
from unittest.mock import patch
import drinkAPI
import requests


# Create your tests here.

class TestDrinkAPI(TestCase):

    test_drink_db_url = 'test_drink.db'

    #@patch ('drinkAPI.call_drink_api')
    def test_drink_api_call(self):
        responce = requests.get('https://the-cocktail-db.p.rapidapi.com/random.php')

        self.assertTrue(responce.ok)



        




class TestFoodAPI(TestCase):

    test_food_db_url = 'test_food.db'

class TestMediaAPI(TestCase):

    test_media_db_url = 'test_media.db'






