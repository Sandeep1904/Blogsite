from rest_framework import viewsets
from .serializers import PostSerializer
from blog.models import Post
from rest_framework import permissions

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticated]