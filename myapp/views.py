from django.shortcuts import render, get_object_or_404
from .models import Dish, Restaurant
from django.core.paginator import Paginator
import pandas as pd
import json


def home(request):
  # df = pd.read_csv('myapp/restaurants.csv')
  # for index, row in df.iterrows():
  #   location = None
  #   cuisine = None
  #   rating = None
  #   if pd.isna(row['full_details']):
  #     print(f"Row {index}: Column 'full_details' is NaN")
  #   else:
  #     print(f"Row {index}: Column 'full_details' is not NaN")
  #     full = json.loads(row.get('full_details'))
  #     dishes = json.loads(row['items'])
  #     id = int(row['id'])
  #     name = row['name']
  #     city = row['location']
  #     coordinates = row['lat_long']
  #     loc = full.get('location', None)
  #     if loc is not None:
  #       location = loc.get('address', None)
  #       cuisine = full.get('cuisines', None)
  #       rating = full.get('user_rating', None).get('aggregate_rating', None)
  #     Restaurant(restaurantId=id, name=name, city=city, location=location, cuisine=cuisine, coordinates=coordinates, rating=rating).save()
  #     rest = get_object_or_404(Restaurant, pk=id)
  #     for key, rate in dishes.items():
  #       print(key, rate)
  #       Dish.objects.create(name=key, rate=rate, restaurant=rest)
  all = Dish.objects.all().order_by('rate')
  paginator = Paginator(all, 20)
  page = request.GET.get('page')
  dishes = paginator.get_page(page)
  context = dict(dishes=dishes)
  return render(request, 'myapp/home.html', context)

def search(request):
  query = request.GET.get('query').strip()
  if query:
    results = Dish.objects.filter(name__icontains=query)
    paginator = Paginator(results, 20)
    page = request.GET.get('page')
    dishes = paginator.get_page(page)
  else:
    dishes = Dish.objects.none()
  data = {'dishes': dishes, 'query': query}
  return render(request, 'myapp/search.html', data)

def dishes(request, id):
  dishes = Dish.objects.get(id=id)
  data = dict(dish=dishes)
  return render(request, 'myapp/dishes.html', data)

def restaurant(request, id):
  rest = Restaurant.objects.get(restaurantId=id)
  dishes = Dish.objects.filter(restaurant=rest)
  data = dict(restaurant=rest, dishes=dishes)
  return render(request, 'myapp/restaurant.html', data)
