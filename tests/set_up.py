from unittest import TestCase

from rest_framework.test import APIClient

from tests.factories import AccountFactory


class AuthenticateUser(TestCase):
    def setUp(self):
        self.user = AccountFactory()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
