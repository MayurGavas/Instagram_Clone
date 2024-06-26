from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class SignUpViewSerializer(ModelSerializer):

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = User.objects.create(**validated_data)
        return user

    class Meta:
        model = User
        fields = ['password', 'username', 'first_name', 'last_name', 'email']

class AllUserViewSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email']


