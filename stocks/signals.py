from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Portfolio


@receiver(post_save, sender=User)
def create_portfolio_for_user(sender, instance, created, **kwargs):
    if created:
        Portfolio.objects.create(owner=instance)
