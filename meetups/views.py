from django.db import IntegrityError
from rest_framework.exceptions import ValidationError

from meetups.models import MeetUp, Tag
from .serializers import MeetUpSerializer, TagSerializer
from rest_framework import generics, permissions
from datetime import datetime


class CreateMeetUpView(generics.CreateAPIView):
    serializer_class = MeetUpSerializer
    permission_classes = (permissions.IsAdminUser,)

    @staticmethod
    def _convert_params_to_list(cs):
        return [int(str_id) for str_id in cs.split(',')]

    def get_queryset(self):
        tags = self.request.query_params.get('tags')
        queryset = self.queryset

        if tags:
            tag_ids = self._convert_params_to_list(tags)
            queryset = self.queryset.filter(tags__id__in=tag_ids)
        return queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except IntegrityError:
            content = {"detail": "MeetUp already exist"}
            raise ValidationError(content)


class MeetUpListView(generics.ListAPIView):
    queryset = MeetUp.objects.all()
    serializer_class = MeetUpSerializer


class MeetUpDetailView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = MeetUp.objects.all()
    serializer_class = MeetUpSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CreateTagView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.AllowAny,)


class UpcomingMeetUPsView(generics.ListAPIView):
    queryset = MeetUp.objects.all()
    serializer_class = MeetUpSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset.filter(start_date__gte=datetime.now())
