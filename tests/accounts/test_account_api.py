from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIClient
from tests.factories import AccountFactory

# accounts:user-register => app_name:name(url)
CREATE_ACCOUNT_ROUTE = reverse('accounts:user-register')
CURRENT_ACCOUNT_ROUTE = reverse('accounts:me')


def generate_account_detail_route(account_id):
    return reverse('accounts:user-detail', args=[account_id])


class AccountPublicAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_payload = {
            "email": "admin@email.com",
            "password": "admin@20189!"
        }
        self.user = AccountFactory()

    def test_create_account_successfully(self):
        res = self.client.post(CREATE_ACCOUNT_ROUTE, self.user_payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_create_account_twice(self):
        AccountFactory(**self.user_payload)
        res = self.client.post(CREATE_ACCOUNT_ROUTE, self.user_payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(res.data['email'][0], 'already exists')

    def test_user_detail(self):
        url = generate_account_detail_route(self.user.id)
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_fetching_user_unauthorized(self):
        res = self.client.get(CURRENT_ACCOUNT_ROUTE)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class AccountPrivateAPITests(TestCase):
    def setUp(self):
        self.user = self.user = AccountFactory()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_fetch_user_successfully(self):
        res = self.client.get(CURRENT_ACCOUNT_ROUTE)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
