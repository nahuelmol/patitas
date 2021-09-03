from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):

	postes	= serializers.PrimaryKeyRelatedField(many=True, read_only=True)

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

	cats		= serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	dogs		= serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	postes		= serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	comments 	= serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	class Meta:
		model = User 
		fields = ('id', 'username', 'dogs', 'postes', 'cats')