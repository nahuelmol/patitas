from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User, Group

@unauthenticated_user
def registerPage(req):
	form = UserForm()

	if req.method == 'POST':
		form = UserForm(req.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='customer')
			user.groups.add(group)
			
			return redirect('login')

	context = {'form':form}
	return render(req,'accounts/register.html',context)

@unauthenticated_user
def loginPage(req):
		
	if req.method == 'POST':
		username = req.POST.get('username')
		password = req.POST.get('password')

		user = authenticate(req,username=username,password=password)
	
		if user is not None:
			login(req,user)
			return redirect('home')
		else:
			messages.info(req,'username or password is incorrect!')
		
	context = {}
	return render(req,'accounts/login.html',context)

def logoutPage(req):
	logout(req)
	return redirect('login')

@login_required(login_url='login')
def profile(req):
	context = {}
	return render(req,'accounts/profiles/profile.html',context)

