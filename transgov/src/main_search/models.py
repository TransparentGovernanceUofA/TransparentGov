from django.conf import settings
from django.db import models
from django.urls.base import reverse
from rest_framework.reverse import reverse as api_reverse

class Subsection(models.Model):
    '''
    The Subsection Model which has been added as a foreign key to the Meeting model.
    '''
    Title = models.CharField(db_index=True, unique=True)
    Items =

class Item(models.Model):
    index_in_pdf =
    separate_index =
    title =
    pages_start =
    pages_end =
    text =
    presenters =
    motions =
    keywords = models.CharField(null=True)
    discussion = models.TextField(db_index=True)
    purpose =

class Motions(models.Model):
    motion =
    carried =
    content =

class Presenters(models.Model):
    name =

     "subsection": [
              { "Title": null,
                "Items": [
                   {
                          "index_in_pdf": null,
                          "separate_index":null,
                          "title":null,
                          "pages_start":null,
                          "pages_end":null,
                          "text":null,
                          "presenters": [ { "name":null } ],
                          "motions": [
                            {
                                "motion":null,
                                "carried":null,
                                "content":null
                            }],
                          "keywords": [ null, null ],
                          "discussion":null,
                          "purpose":null
                    }]
              }]

    def __str__(self):
        return self.name


class Meeting(models.Model):
    '''
    The Meeting Model with its essential fields of the data.
    '''
    filename = models.CharField(db_index=True, default='')
    title = models.CharField(unique=True, max_length=255, db_index=True, default='')
    date = models.CharField(db_index=True, default='')
    committee = models.CharField(db_index=True, max_length=255, default='')
    time = models.CharField(db_index=True, default='')
    location = models.CharField(db_index=True, default='')
    attendees = model.TextField(db_index=True)
    subsection = model.TextField(db_index=True)
    slug = models.SlugField(null=True, blank=True, unique=True, max_length=255)
    description = models.TextField(db_index=True)
    committee = models.CharField(db_index=True, max_length=255)
    category = models.ForeignKey('Category', related_name='category')


    def __str__(self):
        return self.title

    def get_api_url(self, request=None):
        return api_reverse("meetings:meeting-rud", kwargs={'pk': self.pk}, request=request)
