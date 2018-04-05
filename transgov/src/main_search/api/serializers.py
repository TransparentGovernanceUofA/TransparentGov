from rest_framework import serializers
from main_search.models import Meeting

class MeetingSerializer(serializers.ModelSerializer):

    '''
    Create a Meeting Serializer class with fields that correspond to the Meeting Model fields.
    url serves as the pk/id
    get_url method:
    returns a full url for the meeting object. Request is passed from MeetingRUDView.
    '''

    class Meta:
        model = Meeting
        fields = [
            'committee',
            'date',
            'title',
            'location',
            'time',
            'attendees',
            'items',
            'url',
        ]
