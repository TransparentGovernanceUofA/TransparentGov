from rest_framework import serializers

from main_search.models import Meeting

class MeetingSerializer(serializers.ModelSerializer):
    url         = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Meeting
        fields = [
            'url',
            'pk',
            'title',
            'slug',
            'description',
            'committee',
            'category',
            'timestamp',
        ]
        read_only_fields = ['pk']

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)
