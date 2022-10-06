# at top of file
from django.shortcuts import redirect
from django.views import View
from django.urls import reverse
from django.views.generic.base import TemplateView
from .models import Skin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView


class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"
    
class SkinsList(TemplateView):
    template_name = "skins_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mySearchName = self.request.GET.get("name")
        # If a query exists we will filter by name 
        if mySearchName != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["skins"] = Skin.objects.filter(name__icontains=mySearchName)
            context["stuff_at_top"] = f"Searching through collections for {mySearchName}"
        else:
            context["skins"] = Skin.objects.all()
            context["stuff_at_top"] = "Skins"
        return context

class SkinCreate(CreateView):
    model = Skin
    fields = ['name', 'img', 'price']
    template_name = "skin_create.html"
    success_url = "/skins/"

class SkinDetail(DetailView):
    model = Skin
    template_name = "skin_detail.html"

class SkinUpdate(UpdateView):
    model = Skin
    fields = ['name', 'img', 'price']
    template_name = "skin_update.html"
    success_url = "/skins/"

    def get_success_url(self):
        return reverse('skin_detail', kwargs={'pk': self.object.pk})

class SkinDelete(DeleteView):
    model = Skin
    template_name = "skin_delete_confirmation.html"
    success_url = "/skins/"
