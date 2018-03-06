import datetime
from django.utils import timezone
from haystack import indexes
from haystack.fields import CharField

from .models import Meeting


class MeetingIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(
        document=True, use_template=True,
        template_name='/Users/ceciliaxiang/TransparentGov/transgov/src/templates/search/indexes/Meeting_text.txt')
    title = indexes.EdgeNgramField(model_attr='title')
    description = indexes.EdgeNgramField(model_attr="description", null=True)

    category = indexes.CharField(model_attr='category', faceted=True)

    committee = indexes.CharField(model_attr='committee', faceted=True)

    # for auto complete
    content_auto = indexes.EdgeNgramField(model_attr='title')

    # Spelling suggestions
    suggestions = indexes.FacetCharField()

    @staticmethod
    def prepare_autocomplete(obj):
        return " ".join((
            obj.title, obj.description, obj.category, obj.committee
        ))

    def get_model(self):
        return Meeting

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(timestamp__lte=timezone.now())
