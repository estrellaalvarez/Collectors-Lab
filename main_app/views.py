from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from .models import Skin

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"

#...
class About(TemplateView):
    template_name = "about.html"
    
class Skin:
    def __init__(self, name, image, price):
        self.name = name
        self.image = image
        self.price = price
skins = [
    Skin('Prime Vandal', "https://i.imgur.com/AyWzBcM.png", '$1'),
    Skin('Sentinels of Light Vandal', "https://i.imgur.com/8me3yA5.jpg", '$1'),
]

class SkinsList(TemplateView):
    template_name = "skins_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["skins"] = skins # this is where we add the key into our context object for the view to use
        return context
