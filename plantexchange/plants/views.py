from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView

from .models import Plant, Comment
from .serializers import PlantSerializer, CommentSerializer


class AdsList(ListAPIView):
    serializer_class = PlantSerializer
    queryset = Plant.objects.all()


class CreateAd(CreateAPIView):
    serializer_class = PlantSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class Comments(ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        return serializer.save(name=self.request.user)