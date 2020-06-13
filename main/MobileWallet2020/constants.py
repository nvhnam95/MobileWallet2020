from datetime import timedelta

MIN_TRANSFER_AMOUNT = 0.001

NEW_ACCOUNT_CREATED = 'new_account_create'
DEPOSIT_TO_ACCOUNT = 'deposit_to_account'
TRANSFER_MONEY = 'transfer_money'

# The cycle is not exact
SAVING_ACCOUNT_TYPES = {
    "yearly": {
        "interest_percentage": 7,
        "cycle": timedelta(days=365)
    },
    "quarterly": {
        "interest_percentage": 1.5,
        "cycle": timedelta(days=91)
    },
    "monthly": {
        "interest_percentage": 0.36,
        "cycle": timedelta(days=30)
    },
    "every_minute": {  # This type is for development only
        "interest_percentage": 1,
        "cycle": timedelta(minutes=1)
    }
}
