# Generated by Django 4.1.1 on 2022-09-17 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditems',
            name='food_category',
            field=models.CharField(blank=True, choices=[('Veg', 'Vegetarian'), ('Non-Veg', 'Non-Vegetarian')], max_length=25, null=True),
        ),
    ]
