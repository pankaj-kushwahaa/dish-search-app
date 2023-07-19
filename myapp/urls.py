from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('search', views.search, name='search'),
  path('dish/<int:id>', views.dishes, name='dish-detail'),
  path('restaurant/<int:id>', views.restaurant, name='restaurant-detail'),
]