from rest_framework import serializers

from main_search.models import Motions, Presenters, Items, Subsection, Meeting

class MotionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motions
        fields = [
            'motion',
            'carries',
            'content',
        ]

class PresentersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presenters
        fields = [
            'name',
        ]

class ItemsSerializer(serializers.ModelSerializer):
    presenters = PresentersSerializer(many=True, read_only=True)
    motions = MotionsSerializer(many=True, read_only=True)

    class Meta:
        model = Items
        fields = [
            'index_in_pdf',
            'separate_index',
            'title',
            'pages_start',
            'pages_end',
            'text',
            'presenters',
            'motions',
            'keywords',
            'discussion',
            'purpose'
        ]

class SubsectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motions
        fields = [
            'motion',
            'carried',
            'content',
        ]

class MeetingSerializer(serializers.ModelSerializer):
    '''
    Create a Meeting Serializer class with fields that correspond to the Meeting Model fields.
    url serves as the pk/id

    get_url method:
    returns a full url for the meeting object. Request is passed from MeetingRUDView.
    '''
    subsection = SubsectionSerializer(many=True, read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Meeting
        fields = [
            'url',
            'pk',
            'filename',
            'title',
            'date',
            'committee',
            'time',
            'location',
            'attendees',
            'subsection',
        ]
        read_only_fields = ['pk']

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)
