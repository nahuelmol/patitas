from db.models import Cat, Dog, Comment, Post, Event
from rest_framework import serializers

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