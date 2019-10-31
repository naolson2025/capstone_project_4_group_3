from django.db import models
from django.db.models import CharField, FloatField, DateTimeField, Model

# Create your models here.

# Create a model to make a table in the database for the Weather information
class Weather(Model):
    # column for the date and time
    date = models.DateTimeField()
    #date = ListCharField(base_field=CharField(max_length=100), max_length=(10000))
    # Found the set null on stack overflow
    # column for the temperature in Farinhight
    temp = models.FloatField(null=True, blank=True, default=None)
    #temp = ListCharField(base_field=CharField(max_length=100), max_length=(10000))

    def __str__(self):
        return f'{self.date}, {self.temp}'


class RecipeSearch(Model):
    # save the users search in order to access it across pages
    users_search = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.users_search}'


class FoodRecipe(Model):
    recipe_name = models.CharField(max_length=200)

    url = models.CharField(max_length=200)
    # Found ListCharField in docs https://django-mysql.readthedocs.io/en/latest/model_fields/list_fields.html
    #food_ingredients = ListCharField(base_field=CharField(max_length=100), max_length=(10000))
    food_ingredients = CharField(max_length=200)

    def __str__(self):
        return f'{self.recipe_name}, {self.url}, {self.food_ingredients}'


class DrinkRecipe(Model):
    drink_recipe_name = models.CharField(max_length=200)

    #drink_ingredients = ListCharField(base_field=CharField(max_length=100), max_length=(10000))
    drink_ingredients = CharField(max_length=200)

    #drink_measurements = ListCharField(base_field=CharField(max_length=100), max_length=(10000))
    drink_measurements = CharField(max_length=200)

    def __str__(self):
        return f'{self.drink_recipe_name}, {self.drink_ingredients}, {self.drink_measurements}'
