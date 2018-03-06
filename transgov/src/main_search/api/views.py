from django.db.models import Q
from rest_framework import generics, mixins, viewsets
from .serializers import MeetingSerializer, MeetingSearchSerializer
from .permissions import IsOwnerOrReadOnly
from main_search.models import Meeting
from haystack.query import SearchQuerySet, EmptySearchQuerySet

from drf_haystack.serializers import HaystackSerializer
from drf_haystack.viewsets import HaystackViewSet
from main_search.search_indexes import MeetingIndex

class MeetingAPIView(mixins.CreateModelMixin, generics.ListAPIView):    # DetailView
    lookup_field           = 'pk'
    serializer_class       = MeetingSerializer

    # def get_queryset(self):
    #     qs = Meeting.objects.all()
    #     query = self.request.GET.get("q")
    #     if query is not None:
    #         qs = qs.filter(
    #                 Q(title__icontains=query)|
    #                 Q(description__icontains=query)
    #                 ).distinct()
    #     return qs

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


# for haystack
class MeetingSearchViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = MeetingSearchSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
    def get_queryset(self):
        request = self.request
        queryset = EmptySearchQuerySet()

        if request.GET.get('q', ''):
            query = request.GET.get('q', '')
            queryset = SearchQuerySet().filter(content=query)
        return queryset


class MeetingRUDView(generics.RetrieveUpdateDestroyAPIView):    # DetailView
    lookup_field        = 'pk'
    serializer_class    = MeetingSerializer
    permission_classes  = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Meeting.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     return Meeting.objects.get(pk=pk)

class MeetingSerializer(HaystackSerializer):
    class Meta:
        index_classes = [MeetingIndex]
        fields = [
            "title", "desciption", "catogory", "committee",
            "content_auto", "suggestions"
        ]

# ViewSet
class MeetingSearchView(HaystackViewSet):
    index_models = [Meeting]
    serializer_class = MeetingSerializer
