from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework import viewsets, permissions, status
from django.contrib.auth.models import User
from . models import Profile, Post, Comment
from . serializers import ProfileSerializer, PostSerializer, CommentSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = [permissions.IsAuthenticated]
    
    # def perform_create(self, serializer):
    #     if Profile.objects.filter(user=self.request.user).exists():
    #         return Response({"detail": "Profile already exists for this user."}, status=status.HTTP_400_BAD_REQUEST)
    #     serializer.save(user=self.request.user)
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    
