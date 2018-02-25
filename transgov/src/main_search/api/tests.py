from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model
# automated
# new / blank db

from main_search.models import Meeting, Category
from django.db import models
User = get_user_model()

class MeetingAPITestCase(APITestCase):
    def setUp(self):
        user_obj = User(username='testuser', email='test@test.com')
        user_obj.set_password("testpassward")
        user_obj.save()
        meeting = Meeting.objects.create(
                title="Test Case Title",
                slug="Test Case slug",
                description="Test Case Description",
                committee="XYZ",
                category=Category.objects.get(category=1)
                )

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)
