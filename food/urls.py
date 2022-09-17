from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('foods', views.display_foods),
    path('foods/<str:val>/', views.filter_food_category),
    path('foods/check/<str:food_name>/', views.get_stock_details),
    path('checkout/', views.checkout),

]
