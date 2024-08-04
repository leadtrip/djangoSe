from django.db import models


class Country(models.Model):
    id = models.BigIntegerField
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "country"


class City(models.Model):
    id = models.BigIntegerField
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "city"


class Continent(models.Model):
    id = models.BigIntegerField
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "continent"
