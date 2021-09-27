from rest_framework import serializers
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

from users.utils import generate_access_token

class RegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'email', 'password')

	def create(self, validated_data):

		print(validated_data)

		user = User(
				email=validated_data['email'],
				username=validated_data['username']
				)
		user.set_password(validated_data['password'])
		user.save()
		
		return user


class UserCreateSerializer(serializers.ModelSerializer):

	#postes	= serializers.PrimaryKeyRelatedField(many=True, read_only=True, )

	class Meta:
		model = User
		fields = ('username', 'email', 'password')
		extra_kwargs = {'password': {'write_only': True, 'required': True}}

	def create(self, validated_data):
			user = User(
				email=validated_data['email'],
				username=validated_data['username']
				)
			user.set_password(validated_data['password'])
			user.save()
			
			Token.objects.create(user=user)
			return user
	

class UserListSerializer(serializers.ModelSerializer):

	class Meta:
		model = User 
		fields = ('id', 'username')