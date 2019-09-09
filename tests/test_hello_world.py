from django.contrib.auth.models import User
from django.test import TestCase


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(
            email='admin@email.com',
            username='username123',
            password='password!234')

    def test_user_created_successfully(self):
        all_users = User.objects.all()
        self.assertEqual(len(all_users), 1)
