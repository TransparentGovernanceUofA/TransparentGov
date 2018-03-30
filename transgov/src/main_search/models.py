from django.conf import settings
from django.db import models
from django.urls.base import reverse
from rest_framework.reverse import reverse as api_reverse
from django.contrib.postgres.fields import ArrayField, JSONField


# class Attendee(models.Model):
#     name = models.CharField(max_length=255, db_index=True, default='')


# class ApprovalRoute(models.Model):
#     route = models.CharField(max_length=255, db_index=True, default='')
#
#
# class Item(models.Model):
#
#     item_no = models.CharField(max_length=255, db_index=True, default='')
#     title = models.CharField(max_length=255, db_index=True, default='')
#     date = models.CharField(max_length=255, db_index=True, default='')
#     committee = models.CharField(db_index=True, max_length=255, default='')
#     proposed_by = models.CharField(max_length=255, db_index=True, default='')
#     presenter = models.CharField(max_length=255, db_index=True, default='')
#     description = models.TextField(blank=True, null=True)
#
#     approval_route = ArrayField(
#                 models.CharField(max_length=255, db_index=True, default='')
#         )
#
#     final_approver = models.CharField(max_length=255, db_index=True, default='')
#     url = models.CharField(max_length=255, db_index=True, default='')
#
#
# class Meeting(models.Model):
#     committee = models.CharField(db_index=True, max_length=255, default='')
#     date = models.CharField(max_length=255, db_index=True, default='')
#     meeting_title = models.CharField(max_length=255, db_index=True, default='')
#     location = models.CharField(max_length=255, db_index=True, default='')
#     time = models.CharField(max_length=255, db_index=True, default='')
#
#     attendees = ArrayField(
#                 models.CharField(max_length=255, db_index=True, default='')
#         )
#
#     items = ArrayField(
#                 models.ForeignKey('Item', related_name='item')
#         )

class Meeting(models.Model):
    data = JSONField()


    # def __str__(self):
    #     return self.meeting_title
