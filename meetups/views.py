from meetups.models import MeetUp
from .serializers import MeetUpSerializer
from rest_framework import generics, permissions


class CreateMeetUpView(generics.CreateAPIView):
    serializer_class = MeetUpSerializer
    permission_classes = (permissions.IsAdminUser,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MeetUpListView(generics.ListAPIView):
    queryset = MeetUp.objects.all()
    serializer_class = MeetUpSerializer


class MeetUpDetailView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = MeetUp.objects.all()
    serializer_class = MeetUpSerializer
    permission_classes = (permissions.IsAuthenticated,)
