from django.db import models

class Dog(models.Model):
	age			= models.IntegerField()
	weight		= models.FloatField()
	race		= models.CharField()
	heigth		= models.FloatField()
	sex			= models.FloatField()

class Cat(models.Model):
	age			= models.IntegerField()
	weight		= models.FloatField()
	race		= models.CharField()
	heigth		= models.FloatField()
	sex			= models.CharField()

class Post(models.Model):
	username	= models.CharField()
	iconname	= models.CharField()
	time_		= models.IntegerField()
	content		= models.TextField()
	likes		= models.IntegerField()
	responses 	= models.IntegerField()

class Comment(models.Model):
	username	= models.CharField()
	iconname	= models.CharField()
	time_		= models.IntegerField()
	content		= models.TextField()
	likes		= models.IntegerField()
	responses 	= models.IntegerField()

