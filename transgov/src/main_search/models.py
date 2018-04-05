from django.conf import settings
from django.db import models

class Items(models.Model):
    '''
    The Category Model which has been added as a foreign key to the Meeting model.
    '''
    item_no = models.CharField(db_index=True, max_length=255)
    item_title = models.CharField(db_index=True, max_length=255)
    motion = models.TextField(db_index=True)
    action_requested = models.CharField(db_index=True, max_length=255)
    date = models.CharField(db_index=True, max_length=255)
    committee = models.CharField(db_index=True, max_length=255)
    proposed_by = models.CharField(db_index=True, max_length=255)
    presenter = models.CharField(db_index=True, max_length=255)
    description = models.TextField(db_index=True)
    participation = models.TextField(db_index=True)
    approval_route = models.TextField(db_index=True)
    final_approver = models.CharField(db_index=True, max_length=255)


    def __str__(self):
        return self.item_title


class Meeting(models.Model):
    '''
    The Meeting Model with its essential fields of the data.
    '''
    committee = models.CharField(db_index=True, max_length=255)
    date = models.CharField(db_index=True, max_length=255)
    title = models.CharField(unique=True, max_length=255, db_index=True, default='')
    location = models.CharField(db_index=True, max_length=255)
    time = models.CharField(db_index=True, max_length=255)
    attendees = models.CharField(db_index=True, max_length=255)
    items = models.ForeignKey('Items', related_name='item')
    url = models.CharField(db_index=True, max_length=255)


    def __str__(self):
        return self.title
