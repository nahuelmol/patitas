from rest_framework.response import Response
from rest_framework import viewsets

from db.models import Cat, Dog, Comment, Post
from db.api.serializer import CatSerializer, DogSerializer, CommentSerializer, PostSerializer

from toOrder.controller import last_first

from django.shortcuts import render

class CatsView(viewsets.ViewSet):
    @staticmethod
    def list(self):
        queryset        = Cat.objects.all()
        serialized      = CatSerializer(queryset, many=True)

        if queryset:
            ordered_data = last_first(serialized.data)
        return Response(ordered_data) 

class DogsView(viewsets.ViewSet):
    @staticmethod
    def list(self):
        queryset        = Dog.objects.all()
        serialized      = DogSerializer(queryset, many=True)

        if queryset:
            ordered_data = last_first(serialized.data)
        return Response(ordered_data) 

class CommentsView(viewsets.ViewSet):
    @staticmethod
    def list(self):
        queryset        = Comment.objects.all()
        serialized      = CommentSerializer(queryset, many=True)

        if queryset:
            ordered_data = last_first(serialized.data)
        return Response(ordered_data) 

class PostsView(viewsets.ViewSet):
    @staticmethod
    def list(self):
        queryset        = Post.objects.all()
        serialized      = PostSerializer(queryset, many=True)

        if queryset:
            ordered_data = last_first(serialized.data)
        return Response(ordered_data) 