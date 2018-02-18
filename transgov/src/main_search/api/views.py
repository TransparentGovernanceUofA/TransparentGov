from rest_framework import generics
from .serializers import MeetingSerializer
from main_search.models import Meeting

class MeetingRUDView(generics.RetrieveUpdateDestroyAPIView):    # DetailView
    lookup_field = 'pk'
    serializer_class = MeetingSerializer

    def get_queryset(self):
        return Meeting.objects.all()

    def get_object(self):
        pk = self.kwargs.get("pk")
        return Meeting.objects.get(pk=pk)
