from django.contrib.gis.db import models
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


class Location(TimeStampedModel):
    """
    Raw Location representation from the mobile client.
    """
    address = models.CharField(max_length=255)
    country_name = models.CharField(max_length=50)
    locality = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    point = models.PointField()

    def __str__(self):
        return '{}'.format(self.point)


class User(TimeStampedModel, AbstractBaseUser):
    phone = models.CharField(max_length=15, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    profile_picture = models.ImageField(upload_to='profile_pics')
    is_publishing = models.BooleanField(default=False)
    current_location = models.OneToOneField(Location, null=True, blank=True)
    USERNAME_FIELD = 'phone'

    def __str__(self):
        return self.phone


class Venue(models.Model):
    unique_identifier = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=500)
    url = models.URLField()
    point = models.PointField()


class NormalizedLocation(Location):
    venue = models.ForeignKey(Venue)
