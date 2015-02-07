from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from rest_framework_extensions.mixins import PaginateByMaxMixin

from django.shortcuts import redirect

from .models import Location, User
from .serializers import UserSerializer, LocationSerializer

import logging
logging.basicConfig(filename='api.log', level=logging.DEBUG)


class AuthMixin(object):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)


class UserViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  AuthMixin,
                  PaginateByMaxMixin,
                  viewsets.GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    max_paginate_by = 50
    filter_fields = ('age',)


class LocationViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      AuthMixin,
                      PaginateByMaxMixin,
                      viewsets.GenericViewSet):

    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    max_paginate_by = 100
    filter_fields = ('latitude', 'longitude', 'locality', 'postal_code', 'country_name')


def index(request):
    return redirect('/api')
