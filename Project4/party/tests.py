from django.test import TestCase
from django.urls import reverse
import unittest
from unittest.mock import patch
import drinkAPI
import requests


# Create your tests here.

class TestDrinkAPI(TestCase):

    test_drink_db_url = 'test_drink.db'

    def test_drink_api_call(self):
        responce = requests.get('https://the-cocktail-db.p.rapidapi.com/random.php')

        self.assertTrue(responce.ok)



class TestFoodAPI(TestCase):

    test_food_db_url = 'test_food.db'

class TestMediaAPI(TestCase):

    test_media_db_url = 'test_media.db'

class TestHomePageIsEmpty(TestCase):

    def test_load_home_page_shows_empty_list(self):
        response = self.client.get(reverse('get_party_data'))
        self.assertTemplateUsed(response, 'party_templates/search.html')
        #self.assertFalse(response.context[''])

    def test_view_page_with_status_code(self):
        test = self.create_test()
        url = reverse('get_party_data')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(test.title, resp.content)

        












