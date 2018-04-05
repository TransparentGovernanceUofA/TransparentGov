# Adapted from http://www.django-rest-framework.org/api-guide/testing/ and
#              https://github.com/codingforentrepreneurs/REST-API-Basics
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model
from main_search.models import Meeting, Items
from django.db import models
from rest_framework.reverse import reverse as api_reverse
from rest_framework_jwt.settings import api_settings

payload_handler = api_settings.JWT_PAYLOAD_HANDLER
encode_handler = api_settings.JWT_ENCODE_HANDLER

User = get_user_model()

class MeetingAPITestCase(APITestCase):
    '''
    Django API Test index_classes
    Set up:
    Created a user 'testuser' to test; set category to 1 and made a random
    meeting minutes for the test case
    '''

    def setUp(self):
        user_obj = User(username='testuser', email='test@test.com')
        user_obj.set_password("testpassward")
        user_obj.save()
        item = Items.objects.create(
                item_no = "1",
                item_title = "title",
                motion = "THAT GFC Academic Planning Committee recommend to General Faculties Council etc.",
                action_requested = "Approval",
                date = "2017-07-14",
                committee = 'APC',
                proposed_by = 'Luigi Mario',
                presenter = 'Luigi Mario',
                description = 'Mr Mario provided members with an overview of the Mario Bros Theatre etc',
                participation = 'GFC - 2017-04-10',
                approval_route = 'GFC - 2017-04-10, APC - 2017-07-14',
                final_approver = 'GFC'
                )
        meeting = Meeting.objects.create(
                committee = "APC",
                date = "2017-07-14",
                title = "Test Case Title 1",
                location = "SAB",
                time = "2:00 pm - 4:00 pm",
                attendees = "Luigi Mario, Mario Mario, Russ Mario",
                items = Items.objects.get(item_title = "title"),
                url = "path/to/pdf1"
                )

    def test_single_user(self):
        '''
        test case for single user
        '''
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_single_meeting(self):
        '''
        test case for the single meeting
        '''
        meeting_count = Meeting.objects.count()
        self.assertEqual(meeting_count, 1)
