# Adapted from https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing

from django.test import TestCase

# Test cases for django models
from .models import *

class CategoryModelTest(TestCase):
    def setUp(self):
        '''
        Set up category object to be used for testing
        '''
        Category.objects.create(
            name='meeting'
        )

    def test_name_label(self):
        '''
        Test case for the category name
        '''
        category = Category.objects.get(name='meeting')
        field_label = category._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        '''
        Test case for the max length for the category's name
        '''
        category = Category.objects.get(name='meeting')
        max_length = category._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)


class MeetingModelTest(TestCase):
        '''
        Set up Meeting object to be used for testing
        '''
    def setUp(self):
        category = Category.objects.create(
            name='meeting'
        )
        meeting_1 = Meeting.objects.create(
            title = "Test Case Title",
            slug = "Test Case slug",
            description = "Test Case Description",
            committee = "XYZ",
            category = Category.objects.get(name='meeting')
        )
        meeting_2 = Meeting.objects.create(
            description = "Test for default title",
            committee = "ABC",
            category = Category.objects.get(name='meeting')
        )

    def test_title_label(self):
        '''
        Test case for the meeting's title
        '''
        meeting = Meeting.objects.get(title='Test Case Title')
        field_label = meeting._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_slug_label(self):
        '''
        Test case for the meeting's slug
        '''
        meeting = Meeting.objects.get(title='Test Case Title')
        field_label = meeting._meta.get_field('slug').verbose_name
        self.assertEqual(field_label, 'slug')

    def test_description_label(self):
        '''
        Test case for the meeting's description
        '''
        meeting = Meeting.objects.get(title='Test Case Title')
        field_label = meeting._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_committee_label(self):
        '''
        Test case for the meeting's committee
        '''
        meeting = Meeting.objects.get(title='Test Case Title')
        field_label = meeting._meta.get_field('committee').verbose_name
        self.assertEqual(field_label, 'committee')

    def test_category_label(self):
        '''
        Test case for meeting's catogory
        '''
        meeting = Meeting.objects.get(title='Test Case Title')
        field_label = meeting._meta.get_field('category').verbose_name
        self.assertEqual(field_label, 'category')

    def test_num_meetings(self):
        '''
        Test case for number of meetings
        '''
        meeting_count = Meeting.objects.count()
        self.assertEqual(meeting_count, 2)

    def test_default_title(self):
        '''
        Test the default title
        '''
        meeting = Meeting.objects.get(title='')
        title = meeting.title
        self.assertEqual(title, '')

    def test_title_max_length(self):
        '''
        Test case for the max length for the meeting's title
        '''
        meeting = Meeting.objects.get(title='Test Case Title')
        max_length = meeting._meta.get_field('title').max_length
        self.assertEqual(max_length, 255)

    def test_committee_max_length(self):
        '''
        Test case for the max length for the meeting's committee
        '''
        meeting = Meeting.objects.get(title='Test Case Title')
        max_length = meeting._meta.get_field('committee').max_length
        self.assertEqual(max_length, 255)
