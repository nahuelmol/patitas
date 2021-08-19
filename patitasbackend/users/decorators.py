from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_function):

	def wrapper_function(req, *args, **kwargs):
		if req.user.is_authenticated:
			return redirect('home')
		else:
			return view_function(req, *args, **kwargs)

	return wrapper_function