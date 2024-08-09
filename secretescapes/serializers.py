from rest_framework import serializers
from .models import Country, City, Continent, Sale


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class ContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Continent
        fields = '__all__'


class SaleSerializer(serializers.ModelSerializer):
    territory = serializers.StringRelatedField()

    class Meta:
        model = Sale
        fields = ['id', 'active', 'start', 'end', 'territory']

