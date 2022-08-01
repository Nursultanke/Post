from django.shortcuts import render
from rest_framework import generics

from .models import Posts
from .serializers import PostListSerializer


class PostListAPIView(generics.ListAPIView):
    serializer_class = PostListSerializer
    queryset = Posts.objects.all()


class PostCreateAPIView(generics.CreateAPIView):
    serializer_class = PostListSerializer
    queryset = Posts.objects.all()


class PostUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PostListSerializer
    queryset = Posts.objects.all()
    lookup_field = 'id'