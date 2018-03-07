from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.http import JsonResponse
from django.shortcuts import render
from haystack.generic_views import FacetedSearchView as BaseFacetedSearchView
from haystack.query import SearchQuerySet

from .models import Meeting


class TemplateView(TemplateView):
    template_name = "index.html"

def index(request, path=''):
    """
    Renders the Vue SPA
    """
    return render(request, 'index.html')
