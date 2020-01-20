from unittest import TestCase

from rest_framework.test import APIClient

from tests.factories import AccountFactory, MeetUpFactory, QuestionFactory


class BaseTest(TestCase):
    def setUp(self):
        self.user = AccountFactory()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.meet_up = MeetUpFactory()
        self.question = QuestionFactory()
