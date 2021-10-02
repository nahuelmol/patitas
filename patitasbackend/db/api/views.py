from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.exceptions import APIException, AuthenticationFailed
from rest_framework import permissions, generics, authentication

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import Settings
from django.http import HttpResponse

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
        headers     = request.META

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
        new_cat.save()

        if new_cat:
            response = redirect(headers.get('HTTP_REFERER', '/catcreate'))
            response.data = {'created':'aha'}
            return response
        else:
            response = redirect(headers.get('HTTP_REFERER', '/catcreate'))
            response.data = {'created':'not created'}
            return response

    def list(self,request):
        user_token  = request.COOKIES.get('access_token')
        headers     = request.META 

        if not user_token:
            raise AuthenticationFailed()

        queryset        = Cat.objects.all()

        if queryset:
            serialized      = CatSerializer(queryset, many=True)

            response = redirect(headers.get('HTTP_REFERER', '/dogcreate'))
            response.data = {'cats':serialized.data}
            return response
        else:
            response = redirect(headers.get('HTTP_REFERER', '/dogcreate'))
            response.data = {'created':'not created'}
            return response

    def retrieve(self, request, pk):
        user_token = request.COOKIES.get('access_token')
        if not user_token:
            raise AuthenticationFailed()

        queryset = Cat.objects.all()
        if queryset:
            cat = get_object_or_404(queryset, pk=pk)
            serialized = CatSerializer(cat)
            response = redirect(headers.get('HTTP_REFERER', '/profile'))

            response.data = {'cat':serialized.data}
            return response
        else:
            response = redirect(headers.get('HTTP_REFERER', '/feed'))
            response.data = {'queryset':'there is not a queryset'}
            return response

class DogsListView(viewsets.ViewSet):
    queryset            = Dog.objects.all()
    serializer_class    = DogSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [ authentication.SessionAuthentication]

    def create(self, request):
        user_token  = request.COOKIES.get('access_token')
        headers     = request.META

        payload = jwt.decode(user_token, settings.SECRET_KEY, algorithms=['HS256'])
        user_model = get_user_model()
        user = user_model.objects.filter(id=payload['user_id']).first()

        new_dog = Dog(
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
        new_dog.save()

        if new_dog:
            response = redirect(headers.get('HTTP_REFERER', '/dogcreate'))
            response.data = {'created':'aha'}
            return response
        else:
            response = redirect(headers.get('HTTP_REFERER', '/dogcreate'))
            response.data = {'created':'not created'}
            return response

    def list(self, request):
        queryset        = Dog.objects.all()
        serialized      = DogSerializer(queryset, many=True)
        headers         = request.META

        user_token  = request.COOKIES.get('access_token')

        if not user_token:
            raise AuthenticationFailed("unauthenticated user")

        if not queryset:
            response = redirect(headers.get('HTTP_REFERER', '/feed'))
            response.data = {'queryset':'the queyset is empty'}
            return response

        response = redirect(headers.get('HTTP_REFERER', '/dogs'))
        response.data = serialized.data
        return response


class CommentsView(viewsets.ViewSet):

    authentication_classes = [ authentication.TokenAuthentication]
    permission_classes = [  permissions.IsAuthenticated, 
                            IsUserLoggedIn]

    def create(self):
        user_token  = request.COOKIES.get('access_token')
        headers     = request.META

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

        if new_com:
            response = redirect(headers.get('HTTP_REFERER', '/dogcreate'))
            response.data = {'created':'aha'}
            return response
        else:
            response = redirect(headers.get('HTTP_REFERER', '/dogcreate'))
            response.data = {'created':'not created'}
            return response
        


    def list(self, request):
        queryset        = Comment.objects.all()
        serialized      = CommentSerializer(queryset, many=True)
        headers         = request.META

        user_token  = request.COOKIES.get('access_token')

        if not user_token:
            raise AuthenticationFailed("unauthenticated user")
        if not queryset:
            response = redirect(headers.get('HTTP_REFERER', '/dogs'))
            response.data = {'data':'there is no data'}
            return response

        response = redirect(headers.get('HTTP_REFERER', '/dogs'))
        response.data = {'list':serialized.data}
        return response 

    def retrieve(self, request, pk):
        headers     = request.META
        user_token  = request.COOKIES.get('access_token')

        if not user_token:
            raise AuthenticationFailed("unauthenticated user")

        queryset    = Comment.objects.all()
        comment     = get_object_or_404(queryset, pk=pk)
        serialized  = CommentSerializer(comment)

        if not queryset:
            response = redirect(headers.get('HTTP_REFERER', '/comments'))
            response.data = {'comment':'there is not comment'}
            return response

        response = redirect(headers.get('HTTP_REFERER', '/comment'))
        response.data = {'comment':serialized.data}
        return response

class PostsView(viewsets.ViewSet):
    authentication_classes  = [authentication.TokenAuthentication]
    permission_classes      = [permissions.AllowAny]

    def create(self, request):
        user_token  = request.COOKIES.get('access_token')
        headers     = request.META

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

        if new_post:
            response = redirect(headers.get('HTTP_REFERER', '/post'))
            response.data = {'created':'aha'}
            return response
        else:
            response = redirect(headers.get('HTTP_REFERER', '/'))
            response.data = {'created':'nel'}
            return response

    def list(self, request):
        queryset        = Post.objects.all()
        serialized      = PostListSerializer(queryset, many=True)

        user_token  = request.COOKIES.get('access_token')

        if not user_token:
            raise AuthenticationFailed("unauthenticated user")

        if queryset:
            ordered_data    = last_first(serialized.data)
            response        = Response()

            response.data   = {'posts':ordered_data}
            return response 

        if not queryset:
            context = {'queryset':'there is not a queryset'}
            response = Response()
            response.data = context
            return response

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
        headers     = request.META
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

        if new_event:
            response = redirect(headers.get('HTTP_REFERER', '/event_detail'))
            response.data = {'created':'aha'}
            return response
        else:
            response = redirect(headers.get('HTTP_REFERER', '/events_feed'))
            response.data = {'created':'no, redirecting to all events page'}
            return response

    def list(self, request):
        user_token  = request.COOKIES.get('access_token')
        headers     = request.META

        if not user_token:
            raise AuthenticationFailed()

        queryset        = Event.objects.all()

        if queryset:
            serialized      = EventSerializer(queryset, many=True)
            response = redirect(headers.get('HTTP_REFERER', '/events_feed'))
            response.data   = {'events':serialized.data}
            return response
        else:
            response = redirect(headers.get('HTTP_REFERER', '/feed'))
            response.data = {'queryset':'there is not queryset'}
            return response


    def retrieve(self, request, pk):
        user_token = request.COOKIES.get('access_token')

        if not user_token:
            raise AuthenticationFailed()

        queryset = Event.objects.all()
        if queryset:
            event = get_object_or_404(queryset, pk=pk)
            serialized = EventSerializer(event)

            response = redirect(headers.get('HTTP_REFERER', '/event_detail'))
            response.data = {'going to':'detail'}
            return response
        else:
            response = redirect(headers.get('HTTP_REFERER', '/feed'))
            response.data = {'queryset':'there is not queryset, not event'}
            return response

