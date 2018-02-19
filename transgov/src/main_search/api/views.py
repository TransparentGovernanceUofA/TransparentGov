from django.db.models import Q
from rest_framework import generics, mixins
from .serializers import MeetingSerializer
from main_search.models import Meeting

class MeetingAPIView(mixins.CreateModelMixin, generics.ListAPIView):    # DetailView
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

    def perform_create(self, serializer):
        pass

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class MeetingRUDView(generics.RetrieveUpdateDestroyAPIView):    # DetailView
    lookup_field = 'pk'
    serializer_class = MeetingSerializer

    def get_queryset(self):
        return Meeting.objects.all()

    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     return Meeting.objects.get(pk=pk)
