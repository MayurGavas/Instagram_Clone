from rest_framework.serializers import ModelSerializer
from .models import UserProfile
from django.contrib.auth.models import User



class UserProfileCreateViewSerializer(ModelSerializer):

    def create(self, validated_data):
        user = self.context['user']
        bio = validated_data.get('bio')
        profile_pic = validated_data.get('profile_pic')

        user_profile = UserProfile.objects.create(user=user,bio=bio,profile_pic=profile_pic)
        return user_profile


    class Meta:
        model = UserProfile
        fields = ['bio','profile_pic']
