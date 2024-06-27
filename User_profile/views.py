from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView

from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication


class UserProfileView(viewsets.GenericViewSet,
                      mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    """This is for Creating a User Profile"""
    def perform_create(self, serializer):
        user = self.request.user
        if UserProfile.objects.filter(user=user).exists():
            raise ValidationError("You already have a Profile")
        serializer.save(user=user)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context

    """For Getting a User Profile"""
    def list(self, request, *args, **kwargs):
        #TODO : make changes to Get all User profiles from DB
        user = self.request.user
        queryset = UserProfile.objects.filter(user=user)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    """ Delete and Update Profile are applied automatically as they require PK"""
    #TODO : Research on This




