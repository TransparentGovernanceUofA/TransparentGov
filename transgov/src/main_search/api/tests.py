# Adapted from http://www.django-rest-framework.org/api-guide/testing/ and
#              https://github.com/codingforentrepreneurs/REST-API-Basics
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model
from main_search.models import Meeting, Category
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
        category = Category.objects.create(
            name=1
        )
        meeting = Meeting.objects.create(
                title="Test Case Title",
                slug="Test Case slug",
                description="Test Case Description",
                committee="XYZ",
                category=Category.objects.get(name=1)
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

    def test_get_list(self):
    '''
    test case for getting the meeting list without Admin being authenticated(read-only)
    '''
        data = {}
        url = api_reverse("meetings:meeting-listcreate")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_post_item(self):
    '''
    test the API POST method handler
    '''
        data = {"title":"Some Test Title",
                "slug":"Some Test Case slug",
                "description":"Some Test Case Description",
                "committee":"ABC",
                "category":1}
        url = api_reverse("meetings:meeting-listcreate")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_item(self):
    '''
    test case for API GET method handler without Admin being authenticated(read-only)
    '''
        meeting = Meeting.objects.first()
        data = {}
        url = meeting.get_api_url()
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_item(self):
    '''
    test case for API UPDATE method handler test case
    without Admin being authenticated(HTTP_401_UNAUTHORIZED)
    '''
        meeting = Meeting.objects.first()
        url = meeting.get_api_url()
        data = {"title":"Some Test Title",
                "slug":"Some Test Case slug",
                "description":"Some Test Case Description",
                "committee":"ABC",
                "category":1}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_item_with_user(self):
    '''
    test case for API UPDATE method handler with user
    '''
        meeting = Meeting.objects.first()
        url = meeting.get_api_url()
        data = {"title":"Some Test Title",
                "slug":"Some Test Case slug",
                "description":"Some Test Case Description",
                "committee":"ABC",
                "category":1}
        user_obj = User.objects.first()
        payload = payload_handler(user_obj)
        token_rsp = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_rsp)
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_ownership(self):
    '''
    test case for API UPDATE method handler with ownership
    '''
        owner = User.objects.create(username='testuser2')
        meeting = Meeting.objects.create(
                title="Test Case Title2",
                slug="Test Case slug2",
                description="Test Case Description2",
                committee="APC",
                category=Category.objects.get(name=1)
                )

        user_obj            = User.objects.first()
        self.assertNotEqual(user_obj.username, owner.username)
        payload             = payload_handler(user_obj)
        token_rsp           = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token_rsp)
        url = meeting.get_api_url()
        data = {"title": "Some rando title", "content": "some more content"}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_login_and_update(self):
    '''
    test case for API login
    '''
        data = {
            'username': 'testuser',
            'password': 'testpassward'
        }
        url = api_reverse("api-login")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
