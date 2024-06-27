from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views


# path('more-info/',include('Followers_Following.urls'),name='Followers_Following')
router = DefaultRouter()
router.register('', views.NetworkEdgeView, basename='followandfollowing')


urlpatterns = [
    path('',include(router.urls))
]
