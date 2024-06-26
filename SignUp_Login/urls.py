from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('all-users', views.AllUsersView)

urlpatterns = [
    path('sign_up/', views.post, name='SignUpView'),

    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', TokenObtainPairView.as_view(), name='login'), #--> This internally takes case of Login Mechanism

    path('',include(router.urls))


]