from django.conf.urls import url
from .views import MeetingRUDView, MeetingAPIView

urlpatterns = [
    url(r'^$', MeetingAPIView.as_view(), name='meeting-listcreate'),
    url(r'^(?P<pk>\d+)/$', MeetingRUDView.as_view(), name='meeting-rud'),
]
