from django.db import models

# Create your models here.

# Create a model to make a table in the database for the Weather information
class Weather(models.Model):
    # column for the date and time
    date = models.DateTimeField()
    # Found the set null on stack overflow
    # column for the temperature in Farinhight
    temp = models.FloatField(null=True, blank=True, default=None)
    # column for the weather
    weather = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.date}, {self.temp}, {self.weather}'