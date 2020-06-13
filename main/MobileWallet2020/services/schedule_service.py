from apscheduler.schedulers.background import BackgroundScheduler
from django.utils import timezone

from MobileWallet2020.constants import SAVING_ACCOUNT_TYPES
from MobileWallet2020.models import SavingAccount


# This function should be trigger by cron commands
def background_schedule_service():
    try:
        scheduler = BackgroundScheduler()
        scheduler.add_job(update_interest, 'interval', seconds=10)  # For faster audit
        scheduler.start()
    except Exception as e:
        print("Relaunch the schedule service")


def update_interest():
    saving_accounts = SavingAccount.objects.all()
    print("Updating interest of saving accounts")
    # This was not optimized
    for saving_account in saving_accounts:
        print("Calculating interest for saving account %s" % saving_account.id)
        account_age = timezone.now() - saving_account.created_time
        cycle = SAVING_ACCOUNT_TYPES.get(saving_account.saving_type).get('cycle')
        interest_percentage = SAVING_ACCOUNT_TYPES.get(saving_account.saving_type).get('interest_percentage')
        saving_account.interest = (account_age//cycle * interest_percentage * saving_account.balance) / 100
        saving_account.save()
        print("Accnout age: %s, saving type: %s, interest: %s" %
              (account_age, saving_account.saving_type, saving_account.interest))
