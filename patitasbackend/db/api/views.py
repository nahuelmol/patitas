from rest_framework.response import Response
from rest_framework import viewsets

from db.models import Cat, Dog, Comment, Post
from db.api.serializer import CatSerializer, DogSerializer, CommentSerializer, PostSerializer, EventSerializer

from toOrder.controller import last_first

class CatsView(viewsets.ViewSet):

    @action(detail=True,methods=['post','get'])
    @staticmethod
    def list(self):
        queryset        = Cat.objects.all()
        serialized      = CatSerializer(queryset, many=True)

        if queryset:
            ordered_data = last_first(serialized.data)
        return Response(ordered_data) 

    @action(detail=True,methods=['post','get'])
    @staticmethod
    def retrieve(self, request, pk):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)

        serialized = UserSerializer(user)
        return Response(serialized.data)

class DogsView(viewsets.ViewSet):

    @action(detail=True,methods=['post','get'])
    @staticmethod
    def list(self):
        queryset        = Dog.objects.all()
        serialized      = DogSerializer(queryset, many=True)

        if queryset:
            ordered_data = last_first(serialized.data)
        return Response(ordered_data) 

    @action(detail=True,methods=['post','get'])
    @staticmethod
    def retrieve(self, request, pk):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)

        serialized = UserSerializer(user)
        return Response(serialized.data)

class CommentsView(viewsets.ViewSet):

    @action(detail=True,methods=['get'])
    @staticmethod
    def list(self):
        queryset        = Comment.objects.all()
        serialized      = CommentSerializer(queryset, many=True)

        if queryset:
            ordered_data = last_first(serialized.data)
        return Response(ordered_data) 

    @staticmethod
    def retrieve(self, request, pk):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)

        serialized = UserSerializer(user)
        return Response(serialized.data)

class PostsView(viewsets.ViewSet):
    @action(detail=True,methods=['get'])
    @staticmethod
    def list(self):
        queryset        = Post.objects.all()
        serialized      = PostSerializer(queryset, many=True)

        if queryset:
            ordered_data = last_first(serialized.data)
        return Response(ordered_data) 

    @staticmethod
    def retrieve(self, request, pk):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)

        serialized = UserSerializer(user)
        return Response(serialized.data)

class EventsView(viewsets.ViewSet):

    @action(detail=True,methods=['get'])
    @staticmethod
    def list(self):
        queryset        = Event.objects.all()
        serialized      = EventSerializer(queryset, many=True)

        return serialized.data

    @staticmethod
    def retrieve(self, request, pk):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)

        serialized = UserSerializer(user)
        return Response(serialized.data)