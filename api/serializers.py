__author__ = 'Greg Ziegan'
from rest_framework import serializers
from rest_framework import pagination
from .models import User, Location


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'phone', 'first_name', 'age', 'profile_picture', 'current_location', 'is_publishing')


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('url', 'point', 'country_name', 'locality', 'postal_code')


class PaginatedUserSerializer(pagination.PaginationSerializer):
    class Meta:
        object_serializer_class = UserSerializer