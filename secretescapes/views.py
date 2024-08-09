import django_filters
from django.views.generic import ListView, DetailView
from .models import Country, City, Continent, Territory, Sale
from rest_framework import generics

from .serializers import CountrySerializer, CitySerializer, SaleSerializer


class AllCountries(ListView):
    model = Country
    template_name = "country/index.html"
    paginate_by = 10
    ordering = "name"


class CountryDetail(DetailView):
    model = Country
    lookup_field = "pk"
    template_name = "area/area_detail.html"


class AllCities(ListView):
    model = City
    template_name = "city/index.html"
    paginate_by = 10
    ordering = "name"

    def get_queryset(self, *args, **kwargs):
        qs = super(AllCities, self).get_queryset(*args, **kwargs)
        qs = qs.exclude(name__exact='')  # there are a number of non-null names that are empty strings
        return qs


class CityDetail(DetailView):
    model = City
    lookup_field = "pk"
    template_name = "area/area_detail.html"


class AllContinents(ListView):
    model = Continent
    template_name = "continent/index.html"
    paginate_by = 10
    ordering = "name"


class ContinentDetail(DetailView):
    model = Continent
    lookup_field = "pk"
    template_name = "area/area_detail.html"


class AllTerritories(ListView):
    model = Territory
    template_name = "territory/index.html"
    paginate_by = 10
    ordering = "name"


class TerritoryDetail(DetailView):
    model = Territory
    lookup_field = "pk"
    template_name = "territory/territory_detail.html"


class AllUkSales(ListView):
    model = Sale
    template_name = "sale/index.html"
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        return Sale.uk_sales.get_queryset()


class SaleDetail(DetailView):
    model = Sale
    lookup_field = "pk"
    template_name = "sale/sale_detail.html"


class CountryListCreate(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CityList(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class SaleList(generics.ListAPIView):
    serializer_class = SaleSerializer
    queryset = Sale.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]   # enables filtering on URL params
    filterset_fields = ["id", "active", "territory"]                        # the list of URL params we allow filtering on


