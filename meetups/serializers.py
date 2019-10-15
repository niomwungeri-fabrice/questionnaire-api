from rest_framework import serializers

from .models import Tag, MeetUp


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'url', 'name']


class MeetUpSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError(
                "End date must be after start date")
        return data

    class Meta:
        model = MeetUp
        fields = ['id', 'name', 'venue', 'image_url', 'user_id',
                  'event_type', 'start_date', 'end_date']
