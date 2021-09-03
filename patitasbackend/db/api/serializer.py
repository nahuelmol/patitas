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

class PostListSerializer(serializers.ModelSerializer):
	class Meta:
		fields	= '__all__'
		model 	= Post 

class PostCreateSerializer(serializers.ModelSerializer):
	
	owner = serializers.IntegerField(source='user', read_only=True)

	class Meta:
		fields	= '__all__'
		model 	= Post 

	def create(self, validated_data):
		post = Post(**validated_data)
		post.save()
		return post

class EventSerializer(serializers.ModelSerializer):

	class Meta:
		fields	= '__all__'
		model 	= Event