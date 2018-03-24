from rest_framework import serializers

from main_search.models import Motions, Presenters, Items, Subsection, Meeting

class MotionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motions
        fields = (
            'motion',
            'carried',
            'content',
        )

class PresentersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presenters
        fields = (
            'name',
        )

class ItemsSerializer(serializers.ModelSerializer):
    presenters = PresentersSerializer(many=True)
    motions = MotionsSerializer(many=True)

    class Meta:
        model = Items
        fields = (
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
        )
    def create(self, validated_data):
        presenter_data = validated_data.pop('name')
        motion_data = validated_data.pop('motion')
        presenter = PresentersSerializer.create(PresentersSerializer(), validated_data=presenter_data)
        motion = MotionsSerializer.create(MotionsSerializer(), validated_data=motion_data)
        p, created = Presenters.objects.update_or_create(name=name)
        m, created = Motions.objects.update_or_create(motion=motion,
                            carried=validated_data.pop('carried'))
        return i


class SubsectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subsection
        fields = (
            'Title',
            'Items',
        )
    def create(self, validated_data):
        item_data = validated_data.pop('title')
        item = ItemsSerializer.create(ItemsSerializer(), validated_data=item_data)
        i, created = Items.objects.update_or_create(title=title,
                            presenters=validated_data.pop('presenters'))
        return i

class MeetingSerializer(serializers.ModelSerializer):
    '''
    Create a Meeting Serializer class with fields that correspond to the Meeting Model fields.
    url serves as the pk/id

    get_url method:
    returns a full url for the meeting object. Request is passed from MeetingRUDView.
    '''
    subsection = SubsectionSerializer(many=True)
    url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Meeting
        fields = (
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
        )
        read_only_fields = ['pk']

    def create(self, validated_data):
        subsection_data = validated_data.pop('Title')
        subsection = SubsectionSerializer.create(SubsectionSerializer(), validated_data=subsection_data)
        sub, created = Subsection.objects.update_or_create(Title=Title,
                            Items=validated_data.pop('Items'))
        return sub

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)
