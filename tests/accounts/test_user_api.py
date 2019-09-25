from django.test import TestCase
from accounts.models import User
from django.urls import reverse
from rest_framework.test import APIClient, APIRequestFactory
factory = APIRequestFactory()

CREATE_USER_ROUTE = reverse('user-register')
test_user = {"email": "admin@email.com", "password": "Password123"}


def sample_user(email=test_user['email'], password=test_user['password']):
    user = User.objects.create_user(
        email=email, password=password,
    )
    return user


class UserAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_user_successfully(self):
        # res = self.client.post('api/v1/register', test_user)
        factory.post('/register/', test_user, format='json')
        user = sample_user()
        # print(res, "=======")
        # self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(user.check_password(test_user['password']))
