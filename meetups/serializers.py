from rest_framework import serializers

from .models import Tag, MeetUp


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'url', 'name']


class MeetUpSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if not data['event_type']:
            raise serializers.ValidationError("Event Type is Required")
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError(
                "End date must be after start date")
        return data

    class Meta:
        model = MeetUp
        fields = ['id', 'name', 'location', 'image_url', 'user_id',
                  'event_type', 'date']
