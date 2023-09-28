from rest_framework import serializers
from rest_framework.exceptions import ValidationError

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
        fields = (
            'id', "title", "descriptions", "comment_count", "created_at", "modifite_at", 'likes', "category", "tags",
            "comments")

    def get_tags(self, obj_post):
        return obj_post.tag_list


class PostValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=3, max_length=100)
    descriptions = serializers.CharField(required=False, default="No text")
    category = serializers.IntegerField(min_value=1)
    tags = serializers.ListField(required=False, child=serializers.IntegerField(min_value=1))

    def validated_category(self, category):
        # categories = Category.objects.filter(id=category)
        # if not categories:
        #     return ValidationError("Category not found")
        try:
            Category.objects.get(id=category)
        except Category.DoesNotExist:
            raise ValidationError("Category not found")
        return category

    def validated_tags(self, tags):
        # for i in tags:
        #     try:
        #         Tag.objects.get(id=i)
        #     except Tag.DoesNotExist:
        #         raise ValidationError("")
        filtered_tags = Tag.objects.filter(id__in=tags)
        if len(tags) != len(filtered_tags):
            raise ValidationError("Tag not found")
        return tags
