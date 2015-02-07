__author__ = 'Greg Ziegan'
from rest_framework import serializers
from .models import User, Location


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('phone', 'url', 'first_name', 'age', 'profile_picture')


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('latitude', 'longitude', 'country_name', 'locality', 'postal_code')