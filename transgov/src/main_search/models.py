import re
from django.conf import settings
from django.db import models
from django.urls.base import reverse
from rest_framework.reverse import reverse as api_reverse
from .search import MeetingIndex

class Category(models.Model):
    name = models.CharField('name', max_length=255, db_index=True, unique=True)
    slug = models.SlugField(unique=True, max_length=100, editable=False)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = verbose_name
        ordering = ['name', 'id']

    def __str__(self):
        return '%s' % self.name

    def save(self, *args, **kwargs):
        slug = self.name.replace(' ', '_').lower()
        slug = re.sub(r'\W+', '', slug)
        self.slug = '_'.join(slug)[:100]
        super(Category, self).save(*args, **kwargs)

    def get_entry_count(self):
        return self.entry_set.select_related().count()


class Meeting(models.Model):
    title = models.CharField('title', unique=True, max_length=255, db_index=True, default='')
    slug = models.SlugField(null=True, blank=True, unique=True, max_length=255)
    description = models.TextField('content', db_index=True)
    committee = models.CharField(db_index=True, max_length=255)
    category = models.ForeignKey(Category, null=True, related_name='category', verbose_name='Category')
    timestamp = models.DateTimeField(auto_now=True)
    read_num = models.IntegerField('views', default=0, editable=False)

    class Meta:
        verbose_name = "meeting"
        verbose_name_plural = verbose_name
        ordering = ['-timestamp', 'id']

    def __str__(self):
        eturn '%s' % self.title

    def save(self, *args, **kwargs):
        title = self.title.replace(' ', '_').lower()
        type_index = title.find(']')
        if type_index > 0:
            title = title[type_index + 1:]
        title = re.sub(r'\W+', '', title)
        self.slug = '_'.join(title)[:100]
        super(Meeting, self).save(*args, **kwargs)

    def get_api_url(self, request=None):
        return api_reverse("meetings:meeting-rud", kwargs={'pk': self.pk}, request=request)

    # def indexing(self):
    #     obj = MeetingIndex(
    #         meta={'pk': self.pk},
    #         title=self.title,
    #         slug=self.slug,
    #         description=self.description,
    #         committee=self.committee,
    #         category=self.category.name,
    #         timestamp=self.timestamp
    #     )
    #     obj.save()
    #     return obj.to_dict(include_meta=True)
    def get_synopsis(self):
        synopsis = []
        word_num = 0
        for line in self.description.splitlines(keepends=True):
            if re.match(r'\w+', line):
                synopsis.append(line)
                word_num += len(re.findall(r'[A-Za-z0-9:/.]+|[\u4e00-\u9fa5]', line))
            if word_num > 30 or len(synopsis) > 3:
                break

        synopsis = ''.join(synopsis)

        return self.synopsis
