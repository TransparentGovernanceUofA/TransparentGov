from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.http import JsonResponse
from haystack.generic_views import FacetedSearchView as BaseFacetedSearchView
from haystack.query import SearchQuerySet

from .models import Meeting


class TemplateView(TemplateView):
    template_name = "index.html"
