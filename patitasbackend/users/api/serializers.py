from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		fields	= '__all__'
		model 	= User 