from rest_framework import serializers

from app.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', "title", "descriptions", "created_at", "modifite_at", 'likes')
