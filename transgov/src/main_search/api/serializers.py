from rest_framework import serializers
#
from main_search.models import Meeting
#
# # class AttendeeSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Attendee
# #         fields = [
# #             'name',
# #         ]
# #
# # class ApprovalRouteSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = ApprovalRoute
# #         fields = [
# #             'route',
# #         ]
#
#
# class ItemsSerializer(serializers.ModelSerializer):
#     #approval_route = ApprovalRouteSerializer()
#
#     class Meta:
#         model = Item
#         fields = [
#             'item_no',
#             'title',
#             'date',
#             'committee',
#             'proposed_by',
#             'presenter',
#             'description',
#             'approval_route',
#             'final_approver',
#         ]
#     def create(self, validated_data):
#         # approval_route_data = validated_data.pop('approval_route')
#         # approval_route = ApprovalRouteSerializer.create(ApprovalRouteSerializer(), validated_data=approval_route_data)
#         item, created = Item.objects.update_or_create(
#             item_no=validated_data.pop('item_no'),
#             title=validated_data.pop('title'),
#             date=validated_data.pop('date'),
#             committee=validated_data.pop('committee'),
#             proposed_by=validated_data.pop('proposed_by'),
#             presenter=validated_data.pop('presenter'),
#             description=validated_data.pop('description'),
#             approval_route=validated_data.pop('approval_route'),
#             final_approver=validated_data.pop('final_approver'))
#
#         return item
#
#
# class MeetingSerializer(serializers.ModelSerializer):
#     '''
#     Create a Meeting Serializer class with fields that correspond to the Meeting Model fields.
#     url serves as the pk/id
#
#     get_url method:
#     returns a full url for the meeting object. Request is passed from MeetingRUDView.
#     '''
#     #attendees = AttendeeSerializer()
#     items = ItemsSerializer()
#     #url = serializers.SerializerMethodField(read_only=True)
#     class Meta:
#         model = Meeting
#         fields = [
#             'committee',
#             'meeting_title',
#             'date',
#             'location',
#             'time',
#             'attendees',
#             'items',
#             'url',
#         ]
#         #read_only_fields = ['pk']
#
#     def create(self, validated_data):
#         #attendees_data = validated_data.pop('attendees')
#         item_data = validated_data.pop('items')
#         #attendees = AttendeeSerializer.create(AttendeeSerializer(), validated_data=attendees_data)
#         items = ItemsSerializer.create(ItemsSerializer(), validated_data=item_data)
#         meeting, created = Meeting.objects.update_or_create(
#             committee=validated_data.pop('committee'),
#             meeting_title=validated_data.pop('meeting_title'),
#             date=validated_data.pop('date'),
#             location=validated_data.pop('location'),
#             time=validated_data.pop('time'),
#             attendees=validated_data.pop('attendees'),
#             items=items,
#             url=validated_data.pop('url'))
#
#         return meeting
#
#     # def get_url(self, obj):
#     #     request = self.context.get("request")
#     #     return obj.get_api_url(request=request)


class MeetingSerializer(serializers.ModelSerializer):
    '''
    Create a Meeting Serializer class with fields that correspond to the Meeting Model fields.
    url serves as the pk/id

    get_url method:
    returns a full url for the meeting object. Request is passed from MeetingRUDView.
    '''
    #attendees = AttendeeSerializer()
    #items = ItemsSerializer()
    #url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Meeting
        fields = [
            'data',
        ]
        #read_only_fields = ['pk']

    # def create(self, validated_data):
    #     #attendees_data = validated_data.pop('attendees')
    #     item_data = validated_data.pop('items')
    #     #attendees = AttendeeSerializer.create(AttendeeSerializer(), validated_data=attendees_data)
    #     items = ItemsSerializer.create(ItemsSerializer(), validated_data=item_data)
    #     meeting, created = Meeting.objects.update_or_create(
    #         committee=validated_data.pop('committee'),
    #         meeting_title=validated_data.pop('meeting_title'),
    #         date=validated_data.pop('date'),
    #         location=validated_data.pop('location'),
    #         time=validated_data.pop('time'),
    #         attendees=validated_data.pop('attendees'),
    #         items=items,
    #         url=validated_data.pop('url'))
    #
    #     return meeting

    # def get_url(self, obj):
    #     request = self.context.get("request")
    #     return obj.get_api_url(request=request)
