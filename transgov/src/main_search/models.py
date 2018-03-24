from django.conf import settings
from django.db import models
from django.urls.base import reverse
from rest_framework.reverse import reverse as api_reverse
from django.contrib.postgres.fields import ArrayField

class Motions(models.Model):
    motion = models.CharField(max_length=255, db_index=True, default='')
    carried = models.CharField(max_length=255, db_index=True, default='')
    content = models.CharField(max_length=255, db_index=True, default='')

class Presenters(models.Model):
    name = models.CharField(max_length=255, db_index=True, default='')

    def __str__(self):
        return self.name

class Items(models.Model):
    index_in_pdf = models.CharField(max_length=255, db_index=True, default='')
    separate_index = models.CharField(max_length=255, db_index=True, default='')
    title = models.CharField(max_length=255, db_index=True, default='')
    pages_start = models.CharField(max_length=255, db_index=True, default='')
    pages_end = models.CharField(max_length=255, db_index=True, default='')
    text = models.CharField(max_length=255, db_index=True, default='')
    presenters = models.ManyToManyField(Presenters)
    motions = models.ManyToManyField(Motions)
    keywords = models.CharField(max_length=255, null=True)
    discussion = models.TextField(max_length=255, db_index=True)
    purpose = models.CharField(max_length=255, null=True)

class Subsection(models.Model):
    '''
    The Subsection Model which has been added as a foreign key to the Meeting model.
    '''
    Title = models.CharField(max_length=255, db_index=True, unique=True)
    Items = models.ManyToManyField(Items)



class Meeting(models.Model):
    '''
    The Meeting Model with its essential fields of the data.
    '''
    filename = models.CharField(max_length=255, db_index=True, default='')
    title = models.CharField(unique=True, max_length=255, db_index=True, default='')
    date = models.CharField(max_length=255, db_index=True, default='')
    committee = models.CharField(db_index=True, max_length=255, default='')
    time = models.CharField(max_length=255, db_index=True, default='')
    location = models.CharField(max_length=255, db_index=True, default='')
    #attendees = models.CharField(max_length=255, db_index=True, default='')

    attendees = ArrayField(
            models.TextField(max_length=255, db_index=True)
    )

    subsection = models.ManyToManyField(Subsection)
    #slug = models.SlugField(null=True, blank=True, unique=True, max_length=255)
    #description = models.TextField(db_index=True)
    #committee = models.CharField(db_index=True, max_length=255)
    #category = models.ForeignKey('Category', related_name='category')


    def __str__(self):
        return self.title

    def get_api_url(self, request=None):
        return api_reverse("meetings:meeting-rud", kwargs={'pk': self.pk}, request=request)
