from django.db import models
from datetime import datetime
from django_mysql.models import Bit1BooleanField

class Country(models.Model):
    id = models.BigIntegerField
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "country"


class City(models.Model):
    id = models.BigIntegerField
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "city"


class Continent(models.Model):
    id = models.BigIntegerField
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "continent"


class Territory(models.Model):
    id = models.BigIntegerField
    currency = models.CharField(max_length=255)
    locale = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    country_name = models.CharField(max_length=255)

    def __str__(self):
        return self.country_name

    class Meta:
        db_table = "territory"


class UkSaleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            territory_id=1,
            active=True,
            start__lt=datetime.now(),
            end__gt=datetime.now(),
        )


class Sale(models.Model):
    id = models.BigIntegerField
    active = Bit1BooleanField()
    date_created = models.DateTimeField
    start = models.DateTimeField()
    end = models.DateTimeField()
    territory = models.ForeignKey(Territory, on_delete=models.CASCADE)
    objects = models.Manager()
    uk_sales = UkSaleManager()      # custom manager for UK sales

    def __str__(self):
        return f'{self.id}:{self.start}:{self.end}'

    class Meta:
        db_table = "base_sale"
