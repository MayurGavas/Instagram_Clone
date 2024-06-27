from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from .models import NetworkEdge

from .serializers import NetworkEdgeViewSerializer
# Create your views here.
from rest_framework import mixins, status
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

"""
1. Follow a User : CREATE
2. Unfollow a User : DELETE
3. Follower Count : GET
4. Following Count : GET

"""


class NetworkEdgeView(viewsets.GenericViewSet,
                      mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      ):

    queryset = NetworkEdge.objects.all()
    serializer_class = NetworkEdgeViewSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


    def delete(self, request, *args, **kwargs):
        network = NetworkEdge.objects.filter(from_user= request.data['from_user'],to_user= request.data['to_user'])
        if network.exists():
            network.delete()
            message = "User Unfollowed"
        else:
            message = "No edge Found"

        return Response({"data":None, "message": message}, status= status.HTTP_200_OK)

    """To get Following nd Followers Count"""
    #TODO : Create different serializers for followers and following, currently onlt to_user details are populated
    #TODO : Create Count API's Also, for Now we have List.

    def get_queryset(self):

        edge_direction =self.request.query_params['directions']
        if edge_direction == 'followers':
            return self.queryset.filter(to_user=self.request.user)
        elif edge_direction == 'following':
            return self.queryset.filter(from_user=self.request.user)








