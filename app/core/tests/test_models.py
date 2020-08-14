from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test for creating user with email"""
        email = 'boo@moo.foo'
        password = 't'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_user_normalized(self):
        """Test the email for a new user is normalized."""
        email = 'test@foo.moo'
        user = get_user_model().objects.create_user(email, 't')

        self.assertEqual(user.email, email.lower())


    def test_new_user_invalid_email(self):
        """Test creating user with no email."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 't')


    def test_create_new_superuser(self):
        """Test creating superuser."""
        user = get_user_model().objects.create_superuser(
            'foo@boo.goo',
            't'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
