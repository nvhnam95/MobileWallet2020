from django.test import TestCase

from MobileWallet2020.models import Customer
from MobileWallet2020.services import funding_service


class TestFundingService(TestCase):
    def test_make_transfer(self):
        customer_1 = Customer.objects.create(username='test_customer1',
                                             password='123456',
                                             balance=1000)
        customer_2 = Customer.objects.create(username='test_customer2',
                                             password='123456',
                                             balance=1000)

        funding_service.make_transfer(customer_1, customer_2, 100)

        customer_1_balance = Customer.objects.get(username='test_customer1').balance
        customer_2_balance = Customer.objects.get(username='test_customer2').balance
        assert customer_1_balance == 900
        assert customer_2_balance == 1100
