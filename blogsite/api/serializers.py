from rest_framework import routers, serializers, viewsets
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'name',
            'title',
            'blog',
            'date_posted',
        ]