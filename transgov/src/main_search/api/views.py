from django.db.models import Q
from rest_framework import viewsets
from rest_framework import generics, mixins, viewsets
from rest_framework.response import Response
#from rest_framework.decorators import list_route
from .serializers import CategorySerializer, MeetingSerializer
from .permissions import IsOwnerOrReadOnly
from main_search.models import Category, Meeting

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class MeetingViewSet(viewsets.ModelViewSet):
    lookup_field           = 'slug'
    lookup_value_regex     = r'\w+'
    serializer_class       = MeetingSerializer

    def get_queryset(self):
        query_set = Meeting.objects.all()
        category = self.request.query_params.get('category', None)
        #query = self.request.GET.get("q")
        query = self.request.query_params.get("q", None)

        if category is not None:
            query_set = query_set.filter(category__slug=category)

        if q is not None:
            query_set = query_set.filter(timestamp__year=archive[:4], timestamp__month=archive[4:6])

        # if query is not None:
        #     query_set = query_set.filter(
        #             Q(title__icontains=query)|
        #             Q(description__icontains=query)
        #             ).distinct()
        return query_set

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.read_num += 1
        instance.save()
        serializer = self.get_serializer(instance, detail=True)

        return Response(serializer.data)

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

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

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
