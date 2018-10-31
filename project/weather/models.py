#WEATHER MODELS.PY
from django.db import models
from django.utils import timezone
import urllib.request
import json

class Location(models.Model):
    """
    Setup the field to store the data of the city
    """ 
    loc_city = models.CharField(max_length = 50)      
    city_name = models.CharField(max_length = 50)    

    def __str__(self):
        """
        Return the combine data of two variables and loc_city and city_name
        """ 
        return self.loc_city + " " + self.city_name
