# Generated by Django 4.1.1 on 2022-09-17 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('desc', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.FloatField()),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
