from django.conf.urls import url
from .views import MeetingRUDView

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', MeetingRUDView.as_view(), name='meeting')
]
