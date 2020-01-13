from unittest import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from meetups.models import Tag, MeetUp
from meetups.serializers import MeetUpSerializer


def sample_meet_up(user, **kwargs):
    tag = Tag.objects.create(name="Politics")
    defaults = {
        "name": "20th Tech Summit",
        "venue": "Telecom House",
        "event_type": "ATTRACTION",
        "tags": [tag.id]
    }
    defaults.update(kwargs)
    return MeetUp.objects.create(user=user, **defaults)


class MeetUpApiTests(TestCase):
    def test_something(self):
        self.assertEqual(True, True)


class PrivateMeetUpApiTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            email='admin@email.com',
            password='password123',
            is_superuser=True,
            is_staff=True
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_fetch_meet_ups(self):
        # user = sample_meet_up(user=self.user)
        # # print(user,"================")
        # print(user, "=========================")
        tag = Tag.objects.create(name="Politics")

        defaults = {
            "name": "20th Tech Summit",
            "venue": "Telecom House",
            "event_type": "ATTRACTION",
            "tags": [str(tag.id)]
        }
        meet_up = self.client.post('/api/v1/meetups/new/', defaults)
        print(meet_up.data, "==========data")
        res = self.client.get('/api/v1/meetups/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        # sample_meet_up(user=self.user)
        # res = self.client.get("/api/v1/meetups")
        # print(res, "=============res")
        # meet_ups = MeetUp.objects.all()
        # serializer = MeetUpSerializer(meet_ups)
        # self.assertEqual(res.status_code, status.HTTP_200_OK)
        # self.assertEqual(res.data, serializer.data)
