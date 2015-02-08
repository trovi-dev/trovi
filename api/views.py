from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from rest_framework_extensions.mixins import PaginateByMaxMixin
from rest_framework.filters import DjangoFilterBackend
from rest_framework.decorators import list_route
from rest_framework.response import Response

from django.core.paginator import Paginator
from django.shortcuts import redirect

from .models import Location, User
from .serializers import UserSerializer, LocationSerializer, PaginatedUserSerializer

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

    @list_route(methods=['GET'])
    def list_within_radius(self, request, phone=4403285783):
        pnt = User.objects.get(phone=phone).current_location.point
        queryset = User.objects.filter(current_location__point__distance_lte=(pnt, 100), is_publishing=True)
        paginator = Paginator(queryset, 2)
        users = paginator.page(1)
        serializer_context = {'request': request}
        serializer = PaginatedUserSerializer(users, context=serializer_context)
        return Response(serializer.data)


class LocationViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      AuthMixin,
                      PaginateByMaxMixin,
                      viewsets.GenericViewSet):

    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    distance_filter_field = 'point'
    filter_backends = (DjangoFilterBackend,)
    max_paginate_by = 100
    filter_fields = ('point', 'locality', 'postal_code', 'country_name')


def index(request):
    return redirect('/api')
