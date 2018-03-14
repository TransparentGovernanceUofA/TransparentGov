from rest_framework import serializers

from main_search.models import Meeting

class MeetingSerializer(serializers.ModelSerializer):
    '''
    Create a Meeting Serializer class with fields that correspond to the Meeting Model fields.
    url serves as the pk/id

    get_url method:
    returns a full url for the meeting object. Request is passed from MeetingRUDView.
    '''

    url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Meeting
        fields = [
            'url',
            'pk',
            'title',
            'slug'
            'description',
            'committee',
            'category',
            'timestamp',
        ]
        read_only_fields = ['pk']

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)



class MeetingSearchSerializer(serializers.Serializer):
    '''
    A serializer that is for haystack so it can use to serialize and deserialize data
    that corresponds to Meeting objects
    '''
    text = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    category = serializers.CharField()
    committee = serializers.CharField()
