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
        presenter_data = validated_data.pop('presenters')
        motion_data = validated_data.pop('motions')
        presenter = PresentersSerializer.create(PresentersSerializer(), validated_data=presenter_data)
        motion = MotionsSerializer.create(MotionsSerializer(), validated_data=motion_data)
        item, created = Items.objects.update_or_create(index_in_pdf=validated_data.pop('index_in_pdf'),
        separate_index=validated_data.pop('separate_index'),title=validated_data.pop('title'),pages_start=validated_data.pop('pages_start'),pages_end=validated_data.pop('pages_end'),text=validated_data.pop('text'),presenters=presenter,motions=motion, keywords=validated_data.pop('keywords'),discussion=validated_data.pop('discussion'),purpose=validated_data.pop('purpose'))

        return item



class SubsectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subsection
        fields = (
            'Title',
            'Items',
        )
    def create(self, validated_data):
        item_data = validated_data.pop('Items')
        item = ItemsSerializer.create(ItemsSerializer(), validated_data=item_data)
        subsection, created = Subsection.objects.update_or_create(Title=validated_data.pop('Title'), Items=item
                            )
        return subsection

class MeetingSerializer(serializers.ModelSerializer):
    '''
    Create a Meeting Serializer class with fields that correspond to the Meeting Model fields.
    url serves as the pk/id

    get_url method:
    returns a full url for the meeting object. Request is passed from MeetingRUDView.
    '''
    subsection = SubsectionSerializer(many=True)
    #url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Meeting
        fields = (
            'filename',
            'title',
            'date',
            'committee',
            'time',
            'location',
            'attendees',
            'subsection',
        )
        # read_only_fields = ['pk']

    def create(self, validated_data):
        subsection_data = validated_data.pop('subsection')
        subsection = SubsectionSerializer.create(SubsectionSerializer(), validated_data=subsection_data)
        meeting, created = Meeting.objects.update_or_create(filename=validated_data.pop('filename'),
        title=validated_data.pop('title'),date=validated_data.pop('date'),committee=validated_data.pop('committee'),time=validated_data.pop('time'),location=validated_data.pop('location'),attendees=validated_data.pop('attendees'),subsection=subsection)

        return meeting

    # def get_url(self, obj):
    #     request = self.context.get("request")
    #     return obj.get_api_url(request=request)
