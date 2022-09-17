from ast import Import
from django.contrib import admin

from .models import FoodItems
#Register your models here.

admin.site.register(FoodItems)

