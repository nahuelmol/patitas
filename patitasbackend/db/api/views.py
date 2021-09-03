from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework import permissions, generics

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from db.models import Cat, Dog, Comment, Post
from db.api.serializer import CatSerializer, DogSerializer, CommentSerializer, PostSerializer, EventSerializer

from toOrder.controller import last_first

class CatsView(viewsets.ViewSet):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request):

        queryset            = Cat.objects.all()
        serializer_class    = CatSerializer

        permission_classes  = [permissions.IsAuthenticatedOrReadOnly]

        def perform_create(self, serializer):
            serializer.save(publisher=self.request.user)

    def list(self,request):
        queryset        = Cat.objects.all()
        serialized      = CatSerializer(queryset, many=True)
        
        return Response(serialized.data) 

    def retrieve(self, request, pk):
        queryset = Cat.objects.all()
        cat = get_object_or_404(queryset, pk=pk)

        serialized = CatSerializer(cat)
        return Response(serialized.data)

class DogsListView(generics.ListCreateAPIView):
    queryset            = Dog.objects.all()
    serializer_class    = DogSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    #add the current user as a publisher of the dog
    def perform_create(self, serializer):
        serializer.save(publisher=self.request.user)

class CommentsView(viewsets.ViewSet):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self):
        pass

    def list(self):
        queryset        = Comment.objects.all()
        serialized      = CommentSerializer(queryset, many=True)

        if queryset:
            ordered_data = last_first(serialized.data)
        return Response(ordered_data) 

    def retrieve(self, request, pk):
        queryset = Comment.objects.all()
        comment = get_object_or_404(queryset, pk=pk)

        serialized = UserSerializer(comment)
        return Response(serialized.data)

class PostsView(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self):
        pass

    def list(self, request):
        queryset        = Post.objects.all()
        serialized      = PostSerializer(queryset, many=True)

        if queryset:
            ordered_data = last_first(serialized.data)
        return Response(ordered_data) 

    def retrieve(self, request, pk):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)

        serialized = UserSerializer(post)
        return Response(serialized.data)

class EventsView(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self):
        pass

    def list(self, request):
        queryset        = Event.objects.all()
        serialized      = EventSerializer(queryset, many=True)

        return serialized.data

    def retrieve(self, request, pk):
        queryset = Event.objects.all()
        event = get_object_or_404(queryset, pk=pk)

        serialized = UserSerializer(event)
        return Response(serialized.data)