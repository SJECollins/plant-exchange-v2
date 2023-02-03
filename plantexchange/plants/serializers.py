from rest_framework import serializers
from .models import Plant, Comment


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ('id', 'title', 'owner', 'category', 'description', 'image', 'will_trade_for', 'added_on', 'updated_on', 'status')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'ad', 'name', 'body', 'added_on')
