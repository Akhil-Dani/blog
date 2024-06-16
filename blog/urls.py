from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profile', views.ProfileViewSet)
router.register('post', views.PostViewSet)
router.register('comment', views.CommentViewSet)

urlpatterns = router.urls