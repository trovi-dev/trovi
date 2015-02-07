from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class TimeStampedModel(models.Model):
    last_edited = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class User(TimeStampedModel, AbstractBaseUser):
    phone = models.CharField(max_length=15, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    profile_picture = models.ImageField(upload_to='profile_pics')
    USERNAME_FIELD = 'phone'

    def __str__(self):
        return self.phone


class Location(TimeStampedModel):
    """
    Raw Location representation from the mobile client.
    """
    latitude = models.FloatField()
    longitude = models.FloatField()
    country_name = models.CharField(max_length=50)
    locality = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)


"""class NormalizedLocation(TimeStampedModel):
    # address: street, primary number, etc
    pass


class Venue(models.Model):
    pass"""
