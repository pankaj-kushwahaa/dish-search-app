from django.db import models

class Restaurant(models.Model):
	restaurantId = models.BigAutoField(primary_key=True, auto_created=False)
	name = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	location = models.CharField(max_length=500, null=True, blank=True)
	cuisine = models.CharField(max_length=400, null=True, blank=True)
	coordinates = models.CharField(max_length=500)
	rating = models.FloatField()

def __str__(self):
    return self.name
	
class Dish(models.Model):
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	rate = models.CharField(max_length=50)
