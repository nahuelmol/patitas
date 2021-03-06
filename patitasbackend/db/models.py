from django.db import models
from django.contrib.auth.models import User

import datetime

class Event(models.Model):

	class Orientations(models.TextChoices):
		unknown		= 'unknown'
		Funds	 	= 'Fund-raising'
		Awareness	= 'Awareness'
		Meeting		= 'Meeting'

	creator			= models.ForeignKey(User, on_delete=models.CASCADE)

	date_created 	= models.DateTimeField()
	date_to_do 		= models.IntegerField()

	likes			= models.IntegerField(default=0)
	description		= models.TextField(default="none description")
	topic			= models.TextField(	max_length=40,
											choices=Orientations.choices,
											blank=None,
											default='unknown')

class Dog(models.Model):
	class HealthState(models.TextChoices):
		unknown		= 'unknown'
		Serious	 	= 'serious'
		Stable		= 'Stable'
		Critical	= 'Critical'

	publisher	= models.ForeignKey(User, on_delete=models.CASCADE,
									default=0)
	age			= models.IntegerField()
	weight		= models.FloatField()
	race		= models.CharField(max_length = 30)
	heigth		= models.FloatField()
	sex			= models.CharField(max_length = 30)
	description	= models.TextField(default="none description")
	#photo_prof	= models.ImageField(default=None,blank=True,null=True)

	health_state = models.CharField(	max_length=35,
									choices = HealthState.choices,
									blank=None,
									default='unknown')

class Cat(models.Model):

	class HealthState(models.TextChoices):
		unknown		= 'unknown'
		Serious	 	= 'serious'
		Stable		= 'Stable'
		Critical	= 'Critical'

	publisher	= models.ForeignKey(User,on_delete = models.CASCADE,	
									default=0)
	age			= models.IntegerField()
	weight		= models.FloatField()
	race		= models.CharField(max_length = 30)
	heigth		= models.FloatField()
	sex			= models.CharField(max_length = 30)
	description	= models.TextField(default="none description")
	#photo_prof	= models.ImageField()

	health_state = models.CharField(max_length=35,
									choices = HealthState.choices,
									blank=None,
									default='unknown')

class Post(models.Model):
	owner 		= models.ForeignKey(User,
									blank=True,
									null=True, 
									on_delete=models.CASCADE)

	date		= models.DateTimeField(auto_now_add=True)
	content		= models.TextField()
	likes		= models.IntegerField(default=0,)
	responses 	= models.IntegerField(default=0)
	shared		= models.IntegerField(default=0)

class Comment(models.Model):
	owner		= models.ForeignKey(User, on_delete=models.CASCADE,	
									default=0)

	date		= models.DateTimeField(auto_now_add=True)
	username	= models.CharField(max_length = 30)
	iconname	= models.CharField(max_length = 30)
	content		= models.TextField()
	likes		= models.IntegerField()
	responses 	= models.IntegerField()
	shared		= models.IntegerField()

