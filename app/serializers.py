from rest_framework import serializers

from app.models import Post, Category, Tag, Comment


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True)
    class Meta:
        model = Post
        fields = ('id', "title", "descriptions","comment_count", "created_at", "modifite_at", 'likes', "category", "tags", "comments")
    def get_tags(self, obj_post):
        return obj_post.tag_list
