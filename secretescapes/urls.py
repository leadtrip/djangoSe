from django.urls import path
from . import views

urlpatterns = [
    path("countries/", views.AllCountries.as_view(), name=""),
    path("countries/<int:pk>/", views.CountryDetail.as_view(), name="country-detail"),
    path("cities/", views.AllCities.as_view(), name=""),
    path("cities/<int:pk>/", views.CityDetail.as_view(), name="city-detail"),
    path("continents/", views.AllContinents.as_view(), name=""),
    path("continents/<int:pk>/", views.ContinentDetail.as_view(), name="continent-detail"),
]