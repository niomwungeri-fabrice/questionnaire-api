from django.test import TestCase
from rest_framework.test import APIClient
from tests.factories import AccountFactory
from rest_framework import status


class QuestionPrivateAPITests(TestCase):
    def setUp(self):
        self.user = self.user = AccountFactory()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_question_successfully(self):
        res = self.client.post('/api/v1/questions/', {
            'body': "body1038"
        })
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
