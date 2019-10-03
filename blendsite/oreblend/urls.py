from django.urls import path
from .views import HomeView


app_name="oreblend"

urlpatterns = [
    path('home', HomeView.as_view(), name="home"),
]