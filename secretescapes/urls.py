from django.urls import path, re_path
from rest_framework.generics import ListAPIView
from . import views
from .models import Continent
from .serializers import ContinentSerializer

urlpatterns = [
    path("countries/", views.AllCountries.as_view(), name=""),
    path("countries/<int:pk>/", views.CountryDetail.as_view(extra_context={'itemName':'Country'}), name="country-detail"),
    path("cities/", views.AllCities.as_view(), name=""),
    path("cities/<int:pk>/", views.CityDetail.as_view(extra_context={'itemName':'City'}), name="city-detail"),
    path("continents/", views.AllContinents.as_view(), name=""),
    path("continents/<int:pk>/", views.ContinentDetail.as_view(extra_context={'itemName':'Continent'}), name="continent-detail"),
    path("territories/", views.AllTerritories.as_view(), name=""),
    path("territories/<int:pk>/", views.TerritoryDetail.as_view(), name="territory-detail"),
    path("sales/", views.AllUkSales.as_view(), name=""),
    path("sales/<int:pk>/", views.SaleDetail.as_view(), name="sale-detail"),

    # API URLS
    path("api/countries/", views.CountryListCreate.as_view(), name="api-countries-list-create"),
    path("api/cities/", views.CityList.as_view(), name="api-city-list"),
    path("api/continents/", ListAPIView.as_view(queryset=Continent.objects.all(), serializer_class=ContinentSerializer), name="api-continent-list"),
    path("api/sales/", views.SaleList.as_view(), name="api-sale-list"),
]