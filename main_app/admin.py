from django.contrib import admin
from .models import Skin # import the Artist model from models.py
# Register your models here.

admin.site.register(Skin) # this line will add the model to the admin panel
