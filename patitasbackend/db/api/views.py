from rest_framework.response import Response
from rest_framework import viewsets

from db.models import Cat, Dog, Comment, Post
from db.api.serializer import CatSerializer, DogSerializer, CommentSerializer, PostSerializer

from django.shortcuts import render

class CatsView(viewsets.ViewSet):
    @staticmethod
    def list(self):
        queryset        = Cat.objects.all()
        serialized      = CatSerializer(queryset, many=True)
        return Response(serialized.data) 

class DogsView(viewsets.ViewSet):
    @staticmethod
    def list(self):
        queryset        = Dog.objects.all()
        serialized      = DogSerializer(queryset, many=True)
        return Response(serialized.data) 

class CommentsView(viewsets.ViewSet):
    @staticmethod
    def list(self):
        queryset        = Comment.objects.all()
        serialized      = CommentSerializer(queryset, many=True)
        return Response(serialized.data) 

class PostsView(viewsets.ViewSet):
    @staticmethod
    def list(self):
        queryset        = Post.objects.all()
        serialized      = PostSerializer(queryset, many=True)
        return Response(serialized.data) 