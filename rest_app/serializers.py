from rest_framework import serializers

from rest_app.models import Posts


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('id', 'title', 'description', 'date')


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('title', 'description', 'date')


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('title', 'description', 'date')

