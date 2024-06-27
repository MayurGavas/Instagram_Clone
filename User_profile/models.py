from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    bio = models.CharField(max_length=500, null= False)
    profile_pic = models.ImageField(upload_to='profile_pic/',blank=True, null = True)
    user = models.OneToOneField(User, on_delete=models.SET_DEFAULT,default=None,related_name='profile',)





