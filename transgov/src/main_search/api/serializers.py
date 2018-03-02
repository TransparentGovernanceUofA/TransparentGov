from rest_framework import serializers

from main_search.models import Categoty, Meeting


class CategorySerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(source='get_entry_count', read_only=True)

    class Meta:
        model = Category
        fields = ('name', 'slug', 'count')

class MeetingSerializer(serializers.ModelSerializer):
    url         = serializers.SerializerMethodField(read_only=True)
    category = serializers.CharField(source='category.name')
    categorySlug = serializers.CharField(source='category.slug', read_only=True)
    synopsis = serializers.CharField(source='get_synopsis', read_only=True)
    views = serializers.IntegerField(source='read_num')

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
            'categorySlug',
            'synopsis',
            'timestamp',
            'views',
        ]
        read_only_fields = ['pk']

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)
