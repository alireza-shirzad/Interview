from ..models import Post
from .serializers import PostSerializer, RatingSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

class PostListView(generics.ListAPIView):
    serializer_class    = PostSerializer
    queryset            = Post.objects.all()


class RatingCreateView(generics.CreateAPIView):
    serializer_class    = RatingSerializer


