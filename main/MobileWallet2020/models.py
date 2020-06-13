from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

MIN_TRANSFER_AMOUNT = 0.001


class Customer(AbstractUser):
    balance = models.FloatField(validators=[MinValueValidator(0)])
    pass


class Transaction(models.Model):
    sender = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='receiver')
    amount = models.FloatField(validators=[MinValueValidator(MIN_TRANSFER_AMOUNT)])
    created_time = models.DateTimeField(auto_now=True)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
