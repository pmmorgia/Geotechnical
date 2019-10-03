from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView


class HomeView(TemplateView):
    template_name = "oreblend/home.html"


# Create your views here.
