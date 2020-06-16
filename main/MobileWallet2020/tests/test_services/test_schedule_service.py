from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from MobileWallet2020.models import Customer, SavingAccount
from MobileWallet2020.services import schedule_service


class TestScheduleService(TestCase):
    def test_update_interest(self):
        saving_type = 'every_minute'
        now = timezone.now()
        customer = Customer.objects.create(username='test_customer1',
                                           password='123456',
                                           balance=1000)
        saving_account = SavingAccount.objects.create(customer=customer,
                                                      balance=1000,
                                                      saving_type=saving_type,
                                                      interest=0)
        account_type_id = saving_account.id

        saving_account.created_time = now - timedelta(minutes=10)
        saving_account.save()

        schedule_service.update_interest()
        interest = SavingAccount.objects.get(id=account_type_id).interest
        assert interest == 100
