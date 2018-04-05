# Adapted from https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing

from django.test import TestCase

# Test cases for django models
from .models import *

class ItemsModelTest(TestCase):
    def setUp(self):
        '''
        Set up Items object to be used for testing
        '''
        Items.objects.create(
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

    def test_name_label(self):
        '''
        Test case for the Item name
        '''
        item = Items.objects.get(item_title='title')
        field_label = item._meta.get_field('item_title').verbose_name
        self.assertEqual(field_label, "item title")

    def test_name_max_length(self):
        '''
        Test case for the max length for the item's name
        '''
        item = Items.objects.get(item_title='title')
        max_length = item._meta.get_field('item_title').max_length
        self.assertEqual(max_length, 255)


class MeetingModelTest(TestCase):
    '''
    Set up Meeting object to be used for testing
    '''
    def setUp(self):
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
        meeting_1 = Meeting.objects.create(
            committee = "APC",
            date = "2017-07-14",
            title = "Test Case Title 1",
            location = "SAB",
            time = "2:00 pm - 4:00 pm",
            attendees = "Luigi Mario, Mario Mario, Russ Mario",
            items = Items.objects.get(item_title = "title"),
            url = "path/to/pdf1"
        )
        meeting_2 = Meeting.objects.create(
            committee = "GFC",
            date = "2015-05-15",
            location = "SAB",
            time = "2:00 pm - 4:00 pm",
            attendees = "Qutin Mario, Luigi Mario",
            items = Items.objects.get(item_title = "title"),
            url = "path/to/pdf2"
        )

    def test_committee_label(self):
        '''
        Test case for the meeting's committee
        '''
        meeting = Meeting.objects.get(title='Test Case Title 1')
        field_label = meeting._meta.get_field('committee').verbose_name
        self.assertEqual(field_label, 'committee')

    def test_date_label(self):
        '''
        Test case for the meeting's date
        '''
        meeting = Meeting.objects.get(title='Test Case Title 1')
        field_label = meeting._meta.get_field('date').verbose_name
        self.assertEqual(field_label, 'date')

    def test_title_label(self):
        '''
        Test case for the meeting's title
        '''
        meeting = Meeting.objects.get(title='Test Case Title 1')
        field_label = meeting._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_location_label(self):
        '''
        Test case for the meeting's location
        '''
        meeting = Meeting.objects.get(title='Test Case Title 1')
        field_label = meeting._meta.get_field('location').verbose_name
        self.assertEqual(field_label, 'location')

    def test_attendees_label(self):
        '''
        Test case for meeting's attendees
        '''
        meeting = Meeting.objects.get(title='Test Case Title 1')
        field_label = meeting._meta.get_field('attendees').verbose_name
        self.assertEqual(field_label, 'attendees')

    def test_items_label(self):
        '''
        Test case for meeting's attendees
        '''
        meeting = Meeting.objects.get(title='Test Case Title 1')
        field_label = meeting._meta.get_field('items').verbose_name
        self.assertEqual(field_label, 'items')

    def test_url_label(self):
        '''
        Test case for meeting's attendees
        '''
        meeting = Meeting.objects.get(title='Test Case Title 1')
        field_label = meeting._meta.get_field('url').verbose_name
        self.assertEqual(field_label, 'url')

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
        meeting = Meeting.objects.get(title='Test Case Title 1')
        max_length = meeting._meta.get_field('title').max_length
        self.assertEqual(max_length, 255)

    def test_committee_max_length(self):
        '''
        Test case for the max length for the meeting's committee
        '''
        meeting = Meeting.objects.get(title='Test Case Title 1')
        max_length = meeting._meta.get_field('committee').max_length
        self.assertEqual(max_length, 255)
