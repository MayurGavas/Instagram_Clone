from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('profile', views.UserProfileView)

urlpatterns = [
    path('', include(router.urls)),

]

"""
1. Get Profile details
2. Update Profile details
3. Follow a different User
4. Get Follower Count
5. Get Following Count
6. Get Follower List
7. Get Following List """
