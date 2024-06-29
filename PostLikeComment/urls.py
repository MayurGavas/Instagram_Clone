from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post', views.OnlyPostView,basename='post')
router.register('media', views.OnlyMediaView,basename='media')

#router.register('like/', views.LikeView,basename='like')
#router.register('comments/', views.CommentsView,basename='comments')

urlpatterns = [
    path('', include(router.urls)),
]
# path('post-info',include('PostLikeComment.urls'),name='Post_Like_Comment')
