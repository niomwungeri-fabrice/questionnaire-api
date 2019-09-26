from django.test import TestCase
from accounts.models import User

test_user = {"email": "admin@email.com", "password": "Password123"}


def sample_user(email=test_user['email'], password=test_user['password']):
    user = User.objects.create_user(
        email=email, password=password,
    )
    return user


def sample_super_user(email=test_user['email'],
                      password=test_user['password'],
                      is_superuser=True,
                      is_staff=True):
    user = User.objects.create_superuser(
        email=email,
        password=password,
        is_superuser=is_superuser,
        is_staff=is_staff
    )
    return user


class AccountModelTestCase(TestCase):
    def test_user_creation_successfully(self):
        user = sample_user()
        self.assertTrue(user.email, test_user['email'])
        self.assertTrue(user.check_password(test_user['password']))

    def test_super_user_creation_successfully(self):
        user = sample_super_user()
        self.assertTrue(user.email, test_user['email'])
        self.assertTrue(user.check_password(test_user['password']))
        self.assertEqual(user.is_superuser, True)

    def test_super_user_creation_failed(self):
        with self.assertRaises(ValueError):
            sample_super_user(is_superuser=False)

    def test_staff_creation_failed(self):
        with self.assertRaises(ValueError):
            sample_super_user(is_superuser=False, is_staff=False)

    def test_user_with_invalid_email(self):
        with self.assertRaises(ValueError):
            sample_user(email=None, password='2489284kdjf')
