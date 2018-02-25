from django.conf import settings
from django.db import models
from django.urls.base import reverse
from rest_framework.reverse import reverse as api_reverse

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True)

    def __str__(self):
        return self.name


class Meeting(models.Model):
    title = models.CharField(unique=True, max_length=255, db_index=True, default='')
    slug = models.SlugField(null=True, blank=True, unique=True, max_length=255)
    description = models.TextField(db_index=True)
    committee = models.CharField(db_index=True, max_length=255)
    category = models.ForeignKey('Category', related_name='category')
    timestamp = models.DateTimeField(auto_now=True)

    # def get_absolute_url(self):
    #     return reverse('meeting',
    #                    kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    def get_api_url(self, request=None):
        return api_reverse("meetings:meeting-rud", kwargs={'pk': self.pk}, request=request)
