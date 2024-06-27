from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .serializers import SignUpViewSerializer, AllUserViewSerializer
from rest_framework import status
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication



"VIEW FOR CREATING A NEW USER IN DATABASE"
@api_view(['POST'])
def post(request):
    signup_serializer = SignUpViewSerializer(data=request.data)
    response_data = {
        'data': None,
        'errors': None
    }
    if signup_serializer.is_valid():
        user = signup_serializer.save()
        refresh = RefreshToken.for_user(user)

        response_data['data'] = {
            "user": signup_serializer.data,
            "Tokens": {
                "refresh": str(refresh),
                "access": str(refresh.access_token)}
        }
        response_status = status.HTTP_200_OK
    else:
        response_data['errors'] = signup_serializer.errors
        response_status = status.HTTP_400_BAD_REQUEST

    return Response(response_data, status=response_status)

class AllUsersView(viewsets.GenericViewSet, mixins.ListModelMixin):

    queryset = User.objects.all()
    serializer_class = AllUserViewSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]












