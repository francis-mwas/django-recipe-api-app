from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_success(self):
        """Test creating new user with an email is successful"""
        email = "mwas@gmail.com"
        password = "mwas12345"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test new user email is normalized"""
        email = "test@GMAIL.COM"
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_blank_email(self):
        """Test if new user has provided an email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_superuser(self):
        """Test create new super user"""
        user = get_user_model().objects.create_superuser(
            "mwas@gmail.com",
            "test12345"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
