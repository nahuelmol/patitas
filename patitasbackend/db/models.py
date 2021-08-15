from django.db import models

class Dog(models.Model):
	age			= models.IntegerField()
	weight		= models.FloatField()
	race		= models.CharField(max_length = 30)
	heigth		= models.FloatField()
	sex			= models.FloatField()

class Cat(models.Model):
	age			= models.IntegerField()
	weight		= models.FloatField()
	race		= models.CharField(max_length = 30)
	heigth		= models.FloatField()
	sex			= models.CharField(max_length = 30)

class Post(models.Model):
        published       = models.DateTimeField(auto_now_add=True)
	username	= models.CharField(max_length = 30)
	iconname	= models.CharField(max_length = 30)
	time		= models.IntegerField()
	content		= models.TextField()
	likes		= models.IntegerField()
	responses 	= models.IntegerField()
	shared		= models.IntegerField()

class Comment(models.Model):
        published       = models.DateTimeField(auto_now_add=True)
	username	= models.CharField(max_length = 30)
	iconname	= models.CharField(max_length = 30)
	time		= models.IntegerField()
	content		= models.TextField()
	likes		= models.IntegerField()
	responses 	= models.IntegerField()
	shared		= models.IntegerField()

