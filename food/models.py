from django.db import models

# Create your models here.

class FoodItems(models.Model):
    name = models.CharField(max_length=100, null= True, blank=True)
    desc = models.CharField(max_length=100, null= True, blank=True)
    price = models.FloatField()
    available = models.BooleanField(default=True)
    food_category = models.CharField(max_length=25, choices=(('Veg','Vegetarian'), ('Non-Veg', 'Non-Vegetarian')),null= True, blank=True)
    qty = models.IntegerField(null= True, blank=True, default=100)


    def __str__(self):
        return "{}".format(self.name)