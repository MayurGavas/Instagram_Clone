from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response

from .models import Post
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import AllPostView,Mediafileserializer,FullPostDetailsWithMediaSerialiser


#TODO : Combile this OnlyPost and Only Media because we will get a single API while Uploading a post
class OnlyPostView(viewsets.ModelViewSet):
    """
    1. Create a Post
    2. Update a Post
    3. Delete a Post
    4. View All Post of logged-in User
    5. Get No Of likes on a Post
    6. Get all Comments on a Post
    """
    queryset = Post.objects.all()
    serializer_class = AllPostView
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return FullPostDetailsWithMediaSerialiser
        return self.serializer_class



    def list(self, request, *args, **kwargs):
        # TODO : make changes to Get all User profiles from DB
        user = self.request.user
        print(user)
        queryset = Post.objects.filter(posted_by=user)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class OnlyMediaView(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = Mediafileserializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]



#class LikeView():
    """
    1. Like a Post
    2. Unlike a Post
    """
  #  pass

#class CommentsView():
    """
    1. Create Comment on Post
    2. Update a Comment
    3. Delete a Comment
    """
 #   pass


