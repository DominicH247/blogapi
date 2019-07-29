from rest_framework import generics, permissions, viewsets
from django.contrib.auth import get_user_model

from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly
from .models import Post


# class PostList(generics.ListCreateAPIView):
# 	queryset = Post.objects.all()
# 	serializer_class = PostSerializer

# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
# 	permission_classes = (IsAuthorOrReadOnly,)
# 	queryset = Post.objects.all()
# 	serializer_class = PostSerializer

# class UserList(generics.ListCreateAPIView):
# 	queryset = get_user_model().objects.all()
# 	serializer_class = UserSerializer

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
# 	queryset = get_user_model().objects.all()
# 	serializer_class = UserSerializer

# CHANGE TO VIEWSETS

class PostViewSet(viewsets.ModelViewSet):
	"""provides both list view and detail view"""
	permission_classes = (IsAuthorOrReadOnly)
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
	"""provide both list view and detail view"""
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer