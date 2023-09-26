from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import Post
from app.serializers import PostSerializer


# Create your views here.

@api_view(["GET"])
def posts_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["GET"])
def posts_detail_view(request, **kwargs):
    if request.method == "GET":
        posts = Post.objects.get(id=kwargs['pk'])
        serializer = PostSerializer(posts, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)