from django.contrib import admin
from .models import Restaurant, Dish

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
  list_display = ['name', 'city', 'location', 'cuisine', 'rating', 'restaurantId']

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
  list_display = ['name', 'rate', 'restaurant']
