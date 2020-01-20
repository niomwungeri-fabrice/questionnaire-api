from datetime import datetime, timedelta

from rest_framework import status
from meetups.models import MeetUp
from meetups.serializers import MeetUpSerializer
from tests.factories import TagFactory, sample_meet_up
from tests.set_up import BaseTest


class PrivateMeetUpApiTests(BaseTest):

    def test_create_meet_up_successfully(self):
        tag = TagFactory()
        tag2 = TagFactory()
        payload = {
                "name": "Another meeting",
                "venue": "Kenya",
                "event_type": "ATTRACTION",
                "tags": [str(tag.id), str(tag2.id)]
        }
        res = self.client.post("/api/v1/meetups/new/", payload)
        self.assertEqual(res.data['tags'], [tag.id, tag2.id])

    def test_create_meet_ups_duplicates(self):
        sample_meet_up(user=self.user)
        payload = {
            "name": "20th Tech Summit",
            "venue": "Telecom House",
            "event_type": "CLASS_TRAINING_WORKSHOP",
        }
        res = self.client.post("/api/v1/meetups/new/", payload)
        self.assertEqual(res.data['detail'], "MeetUp already exist")
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_with_wrong_dates(self):
        payload = {
            "name": "20th Tech Summit",
            "venue": "Telecom House",
            "event_type": "SEMINAR_OR_TALK",
            "start_date": datetime.now() + timedelta(days=1),
            "end_date": datetime.now()
        }
        res = self.client.post("/api/v1/meetups/new/", payload)
        self.assertEqual(res.data['non_field_errors'][0],
                         "End date must be after start date")
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_fetch_meet_ups_successfully(self):
        res = self.client.get("/api/v1/meetups/")
        meet_ups = MeetUp.objects.all()
        serializer = MeetUpSerializer(meet_ups, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_fetch_upcoming_meet_ups(self):
        res = self.client.get("/api/v1/meetups/upcoming/")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
