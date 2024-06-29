"""
URL configuration for Instagram_Clone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('SignUp_Login.urls'), name='signup_login'),
    path('user-profile/', include('User_profile.urls'), name='Profile_details'),
    path('more-info/',include('Followers_Following.urls'),name='Followers_Following'),
    path('post-info/',include('PostLikeComment.urls'),name='Post_Like_Comment')

]
