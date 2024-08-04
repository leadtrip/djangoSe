from django.urls import path
from . import views

urlpatterns = [
    path("countries/", views.AllCountries.as_view(), name=""),
    path("cities/", views.AllCities.as_view(), name=""),
    path("continents/", views.AllContinents.as_view(), name=""),
]