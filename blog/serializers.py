from rest_framework import serializers
from . models import Profile, Post, Comment
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name' ,'email']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'image']
        
        

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['id' ,'author', 'title','content', 'created_at']
        read_only_fields = ['id' ,'author' ,'created_at']
        
class CommentSerializer(serializers.ModelSerializer):
    authour = UserSerializer(read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all)
    class Meta:
        model = Comment
        fields = ['id', 'post', 'authour', 'text', 'created_at']
        read_only_fields = ['id' ,'authour', 'created_at']