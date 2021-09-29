from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.exceptions import APIException, AuthenticationFailed
from rest_framework import permissions, generics, authentication

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings

from db.permissions import IsUserLoggedIn
from db.models import Cat, Dog, Comment, Post, Event
from db.api.serializer import CatSerializer, DogSerializer, CommentSerializer, EventSerializer
from db.api.serializer import PostListSerializer, PostCreateSerializer

from toOrder.controller import last_first

import jwt

class CatsView(viewsets.ViewSet):

    authentication_classes = [ authentication.TokenAuthentication]
    permission_classes = [  permissions.IsAuthenticatedOrReadOnly, 
                            IsUserLoggedIn]

    def create(self, request):
        user_token  = request.COOKIES.get('access_token')

        payload = jwt.decode(user_token, settings.SECRET_KEY, algorithms=['HS256'])
        user_model = get_user_model()
        user = user_model.objects.filter(id=payload['user_id']).first()

        new_cat = Cat(
            name=request.data.get('name'),
            age=request.data.get('age'),
            race=request.data.get('race'),
            sex=request.data.get('sex'),
            description=request.data.get('description'),
            heigth=request.data.get('heigth'),
            weight=request.data.get('weight'),
            publisher=user,
            health_state=request.data.get('health_state')
            )

        return redirect(reverse('myapi:cats'))

    def list(self,request):
        user_token = request.COOKIES.get('access_token')
        if not user_token:
            raise AuthenticationFailed()

        queryset        = Cat.objects.all()

        if queryset:
            serialized      = CatSerializer(queryset, many=True)
            return Response(serialized.data)
        else:
            data = {'queryset':'there is not queryset'}
            response = Response(data)
            return response 

    def retrieve(self, request, pk):
        user_token = request.COOKIES.get('access_token')
        if not user_token:
            raise AuthenticationFailed()

        queryset = Cat.objects.all()
        if queryset:
            cat = get_object_or_404(queryset, pk=pk)
            serialized = CatSerializer(cat)
            return Response(serialized.data)
        else:
            data = {'queryset':'there is not a queryset'}
            response = Response(data)
            return response

class DogsListView(viewsets.ViewSet):
    queryset            = Dog.objects.all()
    serializer_class    = DogSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [ authentication.SessionAuthentication]

    def create(self, request):
        user_token  = request.COOKIES.get('access_token')

        payload = jwt.decode(user_token, settings.SECRET_KEY, algorithms=['HS256'])
        user_model = get_user_model()
        user = user_model.objects.filter(id=payload['user_id']).first()

        new_cat = Cat(
            name=request.data.get('name'),
            age=request.data.get('age'),
            race=request.data.get('race'),
            sex=request.data.get('sex'),
            description=request.data.get('description'),
            heigth=request.data.get('heigth'),
            weight=request.data.get('weight'),
            publisher=user,
            health_state=request.data.get('health_state')
            )
        return redirect(reverse('myapi:dogs'))

    def list(self, request):
        queryset        = Dog.objects.all()
        serialized      = DogSerializer(queryset, many=True)

        user_token  = request.COOKIES.get('access_token')

        if not user_token:
            raise AuthenticationFailed("unauthenticated user")

        if not queryset:
            data = {'queryset':'the queyset is empty'}
            response = Response(data)
            return response

        return redirect(reverse('myapi:dogs'))


class CommentsView(viewsets.ViewSet):

    authentication_classes = [ authentication.TokenAuthentication]
    permission_classes = [  permissions.IsAuthenticated, 
                            IsUserLoggedIn]

    def create(self):
        user_token  = request.COOKIES.get('access_token')

        if not user_token:
            raise AuthenticationFailed("unauthenticated user")

        payload = jwt.decode(user_token, settings.SECRET_KEY, algorithms=['HS256'])
        user_model = get_user_model()
        user = user_model.objects.filter(id=payload['user_id']).first()

        content     = request.data.get("content")
        new_comm    = Comment(
            owner=user,
            content=content)
        new_comm.save()

        return redirect(reverse('myapi:comments'))


    def list(self, request):
        queryset        = Comment.objects.all()
        serialized      = CommentSerializer(queryset, many=True)

        user_token  = request.COOKIES.get('access_token')

        if not user_token:
            raise AuthenticationFailed("unauthenticated user")

        return Response(serialized.data) 

    def retrieve(self, request, pk):
        queryset = Comment.objects.all()
        comment = get_object_or_404(queryset, pk=pk)

        serialized = CommentSerializer(comment)
        return Response(serialized.data)

class PostsView(viewsets.ViewSet):
    authentication_classes  = [authentication.TokenAuthentication]
    permission_classes      = [permissions.AllowAny]

    def create(self, request):
        user_token  = request.COOKIES.get('access_token')

        if not user_token:
            raise AuthenticationFailed("unauthenticated user")

        payload = jwt.decode(user_token, settings.SECRET_KEY, algorithms=['HS256'])
        user_model = get_user_model()
        user = user_model.objects.filter(id=payload['user_id']).first()

        content     = request.data.get("content")
        new_post    = Post(
            owner=user,
            content=content)
        new_post.save()

        return redirect(reverse('myapi:posts'))

    def list(self, request):
        queryset        = Post.objects.all()
        serialized      = PostListSerializer(queryset, many=True)

        user_token  = request.COOKIES.get('access_token')

        if not user_token:
            raise AuthenticationFailed("unauthenticated user")

        if queryset:
            ordered_data = last_first(serialized.data)
            return Response(ordered_data) 
        if not queryset:
            context = {'queryset':'there is not a queryset'}
            return Response(context)

    def retrieve(self, request, pk):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)

        user_token  = request.COOKIES.get('access_token')

        if not user_token:
            raise AuthenticationFailed("unauthenticated user")

        serialized = UserSerializer(post)
        return Response(serialized.data)

class EventsView(viewsets.ViewSet):
    permission_classes      = [permissions.AllowAny]
    authentication_classes  = [authentication.TokenAuthentication]

    def create(self):
        user_token  = request.COOKIES.get('access_token')

        if not user_token:
            raise AuthenticationFailed()

        payload = jwt.decode(user_token, settings.SECRET_KEY, algorithms=['HS256'])
        user_model = get_user_model()
        user = user_model.objects.filter(id=payload['user_id']).first()

        new_event = Event(
            creator=user,
            date_to_do=request.data.get('date_to_do'),
            topic=request.data.get('data')
            )
        new_event.save()

        return redirect(reverse('myapi:events'))

    def list(self, request):
        user_token = request.COOKIES.get('access_token')

        if not user_token:
            raise AuthenticationFailed()

        queryset        = Event.objects.all()

        if queryset:
            serialized      = EventSerializer(queryset, many=True)
            return Response(serialized.data)
        else:
            data = {'queryset':'there is not queryset'}
            response = Response(data)
            return response


    def retrieve(self, request, pk):
        user_token = request.COOKIES.get('access_token')

        if not user_token:
            raise AuthenticationFailed()

        queryset = Event.objects.all()
        if queryset:
            event = get_object_or_404(queryset, pk=pk)
            serialized = UserSerializer(event)
            return Response(serialized.data)
        else:
            data = {'queryset':'there is not queryset'}
            response = Response(data)
            return response

