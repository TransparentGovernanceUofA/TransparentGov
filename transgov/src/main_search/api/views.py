from django.db.models import Q
from rest_framework import generics, mixins, viewsets
from .serializers import MeetingSerializer, MeetingSearchSerializer
from .permissions import IsOwnerOrReadOnly
from main_search.models import Meeting
from haystack.query import SearchQuerySet, EmptySearchQuerySet

from drf_haystack.serializers import HaystackSerializer
from drf_haystack.viewsets import HaystackViewSet
from main_search.search_indexes import MeetingIndex

class MeetingAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    '''
    Used for read-only endpoints to represent a collection of meeting model instances.
    Used mixins.create(request, *args, **kwargs) to implement creating and saving a new model instance.
    On top of the default 'GET' method handler, added 3 method handlers:
    POST: returns created object),
    PUT: returns updated object)
    and PATCH: returns (partial) updated object

    get_queryset:
    getting the query from the GET method, returns the queryset
    '''

    lookup_field           = 'pk'
    serializer_class       = MeetingSerializer
    
    def get_queryset(self):
        qs = Meeting.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                    Q(title__icontains=query)|
                    Q(description__icontains=query)
                    ).distinct()
        return qs

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class MeetingSearchViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Used mixins.list method to implement a list of queryset.
    """

    serializer_class = MeetingSearchSerializer
    permission_classes = [IsOwnerOrReadOnly]

    # def get_queryset(self):
    #     request = self.request
    #     queryset = EmptySearchQuerySet()
    #
    #     if request.GET.get('q', ''):
    #         query = request.GET.get('q', '')
    #         queryset = SearchQuerySet().filter(content=query)
    #     return queryset


class MeetingRUDView(generics.RetrieveUpdateDestroyAPIView):
    '''
    The RetrieveUpdateDestroyAPIView used for read-write-delete endpoints
    to represent a single model instance.

    permission checks for authentication,
    only allows Admin to POST, PUT, DELETE;
    non-admin user can only use GET.

    get_serializer_context:
    returns the request to be sent to the serializer method
    '''

    lookup_field        = 'pk'
    serializer_class    = MeetingSerializer
    permission_classes  = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Meeting.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

class MeetingSerializer(HaystackSerializer):
    '''
    The `index_classes` attribute is a list of which search indexes
    we want to include in the search.

    # The `fields` contains all the fields we want to include.
    '''

    class Meta:
        index_classes = [MeetingIndex]
        fields = [
            "title", "desciption", "catogory", "committee",
            "content_auto", "suggestions"
        ]


class MeetingSearchView(HaystackViewSet):
    '''
    # `index_models` is a list of which models you would like to include
    in the search result.
    # (Translates to `SearchQuerySet().models(*index_models)` behind the scenes.
    '''

    index_models = [Meeting]
    serializer_class = MeetingSerializer
