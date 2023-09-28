from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import Post
from app.serializers import PostSerializer


# Create your views here.

@api_view(["GET", "POST"])
def posts_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        title = request.data.get('title')
        category = request.data.get("category")
        tags = request.data.get("tags")
        descriptions = request.data.get("descriptions")
        likes = request.data.get("likes")
        post = Post.objects.create(title=title, category=category, descriptions=descriptions, likes=likes)
        post.tags.set(tags)
        post.save()
        return Response(PostSerializer(post).data)


@api_view(["GET", "PUT", "DELETE"])
def posts_detail_view(request, **kwargs):
    try:
        posts = Post.objects.get(id=kwargs['pk'])
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = PostSerializer(posts, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        posts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        posts.title = request.data.get('title')
        posts.category = request.data.get("category")
        posts.tags.set(request.data.get("tags"))
        posts.descriptions = request.data.get("descriptions")
        posts.likes = request.data.get("likes")
        posts.save()
        return Response(PostSerializer(posts).data)
