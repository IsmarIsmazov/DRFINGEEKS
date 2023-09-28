from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import Post
from app.serializers import PostSerializer, PostValidateSerializer


# Create your views here.

@api_view(["GET", "POST"])
def posts_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = PostValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        title = serializer.validated_data.get('title')
        category = serializer.validated_data.get('category')
        tags = serializer.validated_data.get('tags')
        descriptions = serializer.validated_data.get('descriptions')
        likes = serializer.validated_data.get('likes')
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
    elif request.method == "DELETE":
        posts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = PostValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        posts.title = serializer.validated_data.get('title')
        posts.category = serializer.validated_data.get("category")
        posts.tags.set(serializer.validated_data.get("tags"))
        posts.descriptions = serializer.validated_data.get("descriptions")
        posts.likes = serializer.validated_data.get("likes")
        posts.save()
        return Response(PostSerializer(posts).data)
