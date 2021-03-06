from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        list = [1, 2, 3, 4, 5, 6]
        context['list'] = list
        return context



class AboutView(TemplateView):
    template_name = "about.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "Ashar Islam"
        context['country'] = "Bangladesh"
        return context
