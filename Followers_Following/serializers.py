from rest_framework.serializers import ModelSerializer
from .models import NetworkEdge
from SignUp_Login.serializers import AllUserViewSerializer
from User_profile.serializers import UserProfileSerializer
from User_profile.models import UserProfile
from SignUp_Login.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields =['first_name','last_name','username']
class UserProfileSerializer2(ModelSerializer):

    user = UserSerializer()
    class Meta:
        model = UserProfile
        fields = ['bio','profile_pic','user']
class NetworkEdgeViewSerializer(ModelSerializer):

    to_user = UserProfileSerializer2(source='to_user.profile')

    class Meta:
        model = NetworkEdge
        fields = ['from_user', 'to_user']
