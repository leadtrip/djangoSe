from django.views.generic import ListView
from .models import Country, City, Continent


class AllCountries(ListView):
    model = Country
    template_name = "country/index.html"
    paginate_by = 10
    ordering = "name"


class AllCities(ListView):
    model = City
    template_name = "city/index.html"
    paginate_by = 10
    # queryset = City.objects.filter(template_name != "")
    ordering = "name"

    def get_queryset(self, *args, **kwargs):
        qs = super(AllCities, self).get_queryset(*args, **kwargs)
        qs = qs.exclude(name__exact='')
        return qs


class AllContinents(ListView):
    model = Continent
    template_name = "continent/index.html"
    paginate_by = 10
    ordering = "name"
