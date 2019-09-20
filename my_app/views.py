""" from django.shortcuts import render """
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User


class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)
        users = User.objects.all()
        context['users'] = users
        return context
