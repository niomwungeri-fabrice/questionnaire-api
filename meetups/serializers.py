from rest_framework import serializers

from .models import Tag, MeetUp


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class MeetUpSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )

    def validate(self, data):
        if data.get('start_date') and data.get('end_date'):
            if data.get('start_date') > data.get('end_date'):
                raise serializers.ValidationError(
                    "End date must be after start date")
        return data

    class Meta:
        model = MeetUp
        fields = ['id', 'name', 'venue', 'image_url', 'user_id',
                  'event_type', 'start_date', 'end_date', 'tags']
