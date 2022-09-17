from multiprocessing import context
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from .models import FoodItems
from django.db.models import Q

# Create your views here.

def home(request):

    print("Chck")
    foods_gt_5 = FoodItems.objects.filter(qty__gte=5)
    for i in foods_gt_5:
        print (i)
    print('comple')
    return render(request, 'food/home.html')

def display_foods(request):

    foods = FoodItems.objects.all()

    context = {'foods': foods }
    # res = []
    # for i in foods:
    #     res.append(i.name)
    #     print(i.name)
    return render(request, 'food/home.html', context)

def filter_food_category(request, val):
    food_category = FoodItems.objects.filter(food_category=val)
    for i in food_category:
        print(i.name)

    context = {'foods': food_category}
    return render (request, 'food/home.html', context)

def check_qty(food_name):
    print("check qty")
    status = False
    foods = FoodItems.objects.get(name=food_name)

    print(foods)
    if foods.qty < 5:
        print('Less')
        status = False
    else:
        status = True
        print('great')
    return status


def get_stock_details(request, food_name):
    print("get stock")
    status = check_qty(food_name)
    return HttpResponse(status)

def checkout(request):
    val = request.GET['foodqty']
    name = request.GET['itemname']

    # context = {'val':val, 'name':name}
    return render(request, 'food/checkout.html', {'val':val, 'name':name})





    



    
