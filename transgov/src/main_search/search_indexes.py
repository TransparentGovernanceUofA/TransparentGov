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
    # filename = indexes.CharField(model_attr='filename')
    data = indexes.EdgeNgramField(model_attr='data')
    # date = indexes.CharField(model_attr='date')
    # #description = indexes.EdgeNgramField(model_attr="description", null=True)
    #
    # #category = indexes.CharField(model_attr='category', faceted=True)
    #
    # committee = indexes.CharField(model_attr='committee', faceted=True)
    # time = indexes.CharField(model_attr='time')
    # location = indexes.CharField(model_attr='location')
    # attendees = indexes.CharField(model_attr='attendees')
    # subsection = indexes.CharField(model_attr='subsection')
    # # for auto complete
    content_auto = indexes.EdgeNgramField(model_attr='data')

    # Spelling suggestions
    suggestions = indexes.FacetCharField()

    # @staticmethod
    # def prepare_autocomplete(obj):
    #     return " ".join((
    #         obj.title, obj.description, obj.category, obj.committee
    #     ))

    def get_model(self):
        return Meeting

    # def index_queryset(self, using=None):
    #     """
    #     Used when the entire index for model is updated.
    #     """
    #     return self.get_model().objects.filter(timestamp__lte=timezone.now())
