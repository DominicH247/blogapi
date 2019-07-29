from rest_framework import generics, permissions
from django.contrib.auth import get_user_model

from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly
from .models import Post


class PostList(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsAuthorOrReadOnly,)
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class UserList(generics.ListCreateAPIView):
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer
