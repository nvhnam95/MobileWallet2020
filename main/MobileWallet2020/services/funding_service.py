from MobileWallet2020.models import Customer


def make_transfer(sender: Customer, receiver: Customer, amount):
    sender.balance -= amount
    receiver.balance += amount
    sender.save()
    receiver.save()
