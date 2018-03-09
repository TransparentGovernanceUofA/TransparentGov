"""searchapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from main_search.views import TemplateView, index
from .settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import routers
from main_search.api.views import MeetingSearchViewSet, MeetingSearchView



# for haystack
# router = routers.SimpleRouter()
# router.register(r'searchquery', MeetingSearchViewSet, base_name='searchquery')

router = routers.DefaultRouter()
router.register("meeting/search", MeetingSearchView, base_name="meeting-search")
router.register("search/query", MeetingSearchViewSet, base_name='search-query')

urlpatterns = [
    #url(r'^$', HomeView.as_view()),
    url(r'^admin/', admin.site.urls),
    #url(r'^meeting/(?P<slug>[\w-]+)/$', MeetingView.as_view(), name='meeting'),
    #url(r'^search/autocomplete/$', autocomplete),
    #url(r'^find/', FacetedSearchView.as_view(), name='haystack_search'),
    url(r'^api/meetings/', include('main_search.api.urls', namespace='meetings')),
    url(r'^api/query/', include(router.urls, namespace='api-query')),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^api/auth/login', obtain_jwt_token, name='api-login'),
    url(r'^api/v1/', include(router.urls, namespace='api-search')),
    # catch-all pattern for compatibility with the Vue routes. This must be last in the list.
    url(r'^(?P<path>.*)/$', index),
    url(r'^$', index),

] + static(MEDIA_URL, document_root=MEDIA_ROOT)
