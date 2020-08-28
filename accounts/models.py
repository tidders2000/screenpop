
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from groups.models import Groups
from business.models import BusinessProfile


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=254)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Switcher(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    group = models.ForeignKey(Groups, null=True, on_delete=models.SET)
    business_profile = models.ForeignKey(
        BusinessProfile, null=True, on_delete=models.CASCADE)
