from django.urls import path
from . import views

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
]