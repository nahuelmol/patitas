from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIRequestFactory 

from db.api.views import CatsView, DogsListView, CommentsView, EventsView 

class CatTest(APITestCase):
	def setUp(self): 
		self.factory = APIRequestFactory() 
		self.view = CatsView.as_view({'get': 'list'}) 
		self.uri = '/db/cats'

	def test_list(self): 
		request = self.factory.get(self.uri) 
		response = self.view(request)
		self.assertEqual(response.status_code, 200, 'Expected Response Code 200, received {0} instead.' .format(response.status_code))

class DogTest(APITestCase):
	def setUp(self):
		self.factory 	= APIRequestFactory()
		self.view 		= DogsListView.as_view()
		self.uri		= 'db/dogs'

	def test_list(self):
		request		= self.factory.get(self.uri)
		response 	= self.view(request)
		self.assertEqual(response.status_code, 200, 'Expected: 200, but {0} was received'.format(response.status_code))

class AuthApiTestComments(APITestCase):
	#This class test is for those endpoints that mandatory require 
	#authenticatication to see the data they contain

	#for this reason, we have to create a test user, who will have a passwor and token
	#to be analize through all this test

	def setUp(self):
		self.uri		= 'db/comments'
		self.factory 	= APIRequestFactory()
		self.view 		= CommentsView.as_view({'get':'list'})

		self.user 		= self.setup_user()
		self.token 		= Token.objects.create(user=self.user)
		self.token.save()

	@staticmethod
	def setup_user():
		User = get_user_model()
		return User.objects.create_user(
			'test',
			email='testuser@test.com',
			password='test'
			)

	def test_list(self):
		request 	= self.factory.get(self.uri,
			HTTP_AUTHORIZATION='Token {0}'.format(self.token.key))
		request.user= self.user 
		response = self.view(request)
		self.assertEqual(
			response.status_code, 
			200, 
			'Expected Response Code, received {0} instead'.format(response.status_code))


class AuthApiTestEvents(APITestCase):
	
	def setUp(self):
		self.uri		= 'db/events'
		self.factory 	= APIRequestFactory()
		self.view 		= EventsView.as_view({'get':'list'})

		self.user 		= self.setup_user()
		self.token 		= Token.objects.create(user=self.user)
		self.token.save()

	@staticmethod
	def setup_user():
		User = get_user_model()
		return User.objects.create_user(
			'test',
			email='testuser@test.com',
			password='test'
			)

	def test_list(self):
		request 	= self.factory.get(self.uri,
			HTTP_AUTHORIZATION='Token {0}'.format(self.token.key))
		request.user= self.user 
		response = self.view(request)
		self.assertEqual(
			response.status_code, 
			200, 
			'Expected Response Code, received {0} instead'.format(response.status_code))