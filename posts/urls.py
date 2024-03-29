from django.urls import path

from rest_framework.routers import SimpleRouter
from .views import UserViewSet, PostViewSet

# from .views import PostList, PostDetail, UserList, UserDetail

# urlpatterns = [
# 	path('users/', UserList.as_view()),
# 	path('users/<int:pk>/', UserDetail.as_view()),
# 	path('<int:pk>/', PostDetail.as_view()),
# 	path('', PostList.as_view()),
# ]

# USING VIEWSETS AND ROUTERS

router = SimpleRouter()
router.register('users', UserViewSet, base_name='users')
router.register('', PostViewSet, base_name='posts')

urlpatterns = router.urls