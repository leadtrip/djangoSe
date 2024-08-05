from django.views.generic import ListView, DetailView
from .models import Country, City, Continent


class AllCountries(ListView):
    model = Country
    template_name = "country/index.html"
    paginate_by = 10
    ordering = "name"


class CountryDetail(DetailView):
    model = Country
    lookup_field = "pk"
    template_name = "area/area_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['itemName'] = 'Country'
        return context


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['itemName'] = 'City'
        return context


class AllContinents(ListView):
    model = Continent
    template_name = "continent/index.html"
    paginate_by = 10
    ordering = "name"


class ContinentDetail(DetailView):
    model = Continent
    lookup_field = "pk"
    template_name = "area/area_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['itemName'] = 'Continent'
        return context
