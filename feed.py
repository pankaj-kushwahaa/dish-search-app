# import_data.py
import csv
from django.core.management.base import BaseCommand
from myapp.models import Dish

class Command(BaseCommand):
  help = 'Import dish data from CSV'

  def handle(self, *args, **options):
    with open('dishes.csv', 'r') as file:
      reader = csv.reader(file)
      next(reader)  # Skip header row
      for row in reader:
          Dish.objects.create(name=row[0])
