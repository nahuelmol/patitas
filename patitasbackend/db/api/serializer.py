from rest_framework import serializers

from django.contrib.auth.models import User
from db.models import Cat, Dog, Comment, Post, Event


class CatSerializer(serializers.ModelSerializer):
	class Meta:
		fields	= '__all__'
		model 	= Cat 

class DogSerializer(serializers.ModelSerializer):
	class Meta:
		fields	= '__all__'
		model 	= Dog  

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		fields 	= '__all__'
		model 	= Comment

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		fields	= '__all__'
		model 	= Post 

class EventSerializer(serializers.ModelSerializer):
	class Meta:
		fields	= '__all__'
		model 	= Event