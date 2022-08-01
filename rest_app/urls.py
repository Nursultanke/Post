from django.urls import path

from rest_app.views import PostListAPIView, PostCreateAPIView, PostUpdateAPIView

urlpatterns = [
    path('post_list/', PostListAPIView.as_view(), name='post_list'),
    path('post_create/', PostCreateAPIView.as_view(), name='post_create'),
    path('post_update/<int:id>/', PostUpdateAPIView.as_view(), name='post_update')
]
