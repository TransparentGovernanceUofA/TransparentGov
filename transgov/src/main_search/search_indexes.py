import datetime
from django.utils import timezone
from haystack import indexes
from haystack.fields import CharField
from .models import Meeting


class MeetingIndex(indexes.SearchIndex, indexes.Indexable):
    '''
    make a search_indexes for Django haystack to index the search items.
    '''

    text = indexes.EdgeNgramField(
        document=True, use_template=True,
        template_name='/Users/ceciliaxiang/TransparentGov/transgov/src/templates/search/indexes/Meeting_text.txt')
    committee = indexes.CharField(model_attr='committee', faceted=True)
    date = indexes.CharField(model_attr='date', faceted=True)
    title = indexes.EdgeNgramField(model_attr='title')
    location = indexes.CharField(model_attr='location', faceted=True)
    time = indexes.CharField(model_attr='time', faceted=True)
    attendees = indexes.CharField(model_attr='attendees', faceted=True)
    items = indexes.CharField(model_attr='items', faceted=True)
    url = indexes.CharField(model_attr='url', faceted=True)

    def get_model(self):
        return Meeting
