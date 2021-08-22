from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):

	class Orientations(models.TextChoices):
		unknown		= 'unknown'
		Funds	 	= 'Fund-raising'
		Awareness	= 'Awareness'
		Meeting		= 'Meeting'

	team			= models.ManyToManyField(User)

	date_created 	= models.DateTimeField()
	date_to_do 		= models.IntegerField()

	likes			= models.IntegerField()
	description		= models.TextField()
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

	publisher	= models.ForeignKey(User, on_delete=models.CASCADE)
	age			= models.IntegerField()
	weight		= models.FloatField()
	race		= models.CharField(max_length = 30)
	heigth		= models.FloatField()
	sex			= models.CharField(max_length = 30)
	description	= models.TextField()
	photo_prof	= models.ImageField()

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

	publisher	= models.ForeignKey(User,on_delete = models.CASCADE)
	age			= models.IntegerField()
	weight		= models.FloatField()
	race		= models.CharField(max_length = 30)
	heigth		= models.FloatField()
	sex			= models.CharField(max_length = 30)
	description	= models.TextField()
	photo_prof	= models.ImageField()

	health_state = models.CharField(max_length=35,
									choices = HealthState.choices,
									blank=None,
									default='unknown')

class Post(models.Model):
	owner 		= models.ForeignKey(User, on_delete=models.CASCADE)

	date		= models.DateTimeField(auto_now_add=True)
	username	= models.CharField(max_length = 30)
	iconname	= models.CharField(max_length = 30)
	content		= models.TextField()
	likes		= models.IntegerField()
	responses 	= models.IntegerField()
	shared		= models.IntegerField()

class Comment(models.Model):
	owner		= models.ForeignKey(User, on_delete=models.CASCADE)

	date		= models.DateTimeField(auto_now_add=True)
	username	= models.CharField(max_length = 30)
	iconname	= models.CharField(max_length = 30)
	content		= models.TextField()
	likes		= models.IntegerField()
	responses 	= models.IntegerField()
	shared		= models.IntegerField()

