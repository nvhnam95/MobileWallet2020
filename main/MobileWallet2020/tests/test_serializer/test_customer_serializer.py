from django.test import TestCase

from MobileWallet2020.views.customer import CustomerSerializer


class TestCustomerSerializer(TestCase):
    def setUp(self):
        self.valid_password_data = {
            "username": "test_user_1",
            "password": "123456"
        }
        self.invalid_password_data = {
            "username": "test_user_1",
            "password": "123"
        }

    def test_validate_password_negative(self):
        serializer = CustomerSerializer(data=self.valid_password_data)
        assert serializer.is_valid() is True

    def test_validate_password(self):
        serializer = CustomerSerializer(data=self.invalid_password_data)
        assert serializer.is_valid() is False
