# from django.shortcuts import render

# Create your views here.
""" from django.shortcuts import render """
from django.views.generic.base import TemplateView


class Home(TemplateView):
    template_name = "coopecApp/home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)
        title = "Gestion des prêts équipements & individuels"
        post = "Bienvenue sur l'application dédiée de gestion des appuis du PROPACOM Ouest"
        context['title'] = title
        context['post'] = post
        return context
