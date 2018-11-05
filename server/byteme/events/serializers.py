from rest_framework import serializers
from .models import Event
from .tag_serializers import TagSerializer
from accounts.serializers import *

class EventSerializer(serializers.Serializer):
    identifier = serializers.UUIDField(read_only= True, format='hex_verbose')
    creater    = UserProfileSerializer(required = True)
    attendant  = UserProfileSerializer(required = False)
    abstract   = serializers.CharField(required = False, allow_blank=True, max_length=100)
    place      = serializers.CharField(required = False, allow_blank=True, max_length=100)
    time       = serializers.CharField(required = False, allow_blank=True, max_length=100)
    title      = serializers.CharField(required = False, allow_blank=True, max_length=100)
    details    = serializers.CharField(required = False, allow_blank=True, max_length=100)
    tags       = TagSerializer(required = False)
    req        = serializers.CharField(required = False, allow_blank=True, max_length=100)
    speaker    = SpeakerSerializer()
    #TODO poster_image

    def create(self, validated_data):
        event = Event.objects.create(**validated_data)
        event.req = "add"
        event.save()
        return event


    def update(self, instance, validated_data):
        instance.abstractReq = validated_data.get('abstract', instance.abstractReq)
        instance.placeReq    = validated_data.get('place'   , instance.placeReq)
        instance.timeReq     = validated_data.get('time'    , instance.timeReq)
        instance.titleReq    = validated_data.get('title'   , instance.titleReq)
        instance.detailsReq  = validated_data.get('details' , instance.detailsReq)
        # instance.tagsReq
        instance.req         = "mod"
        instance.save()
        return instance