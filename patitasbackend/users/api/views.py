from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.view import APIView

from django.contrib.auth.models import User

from users.api.serializers import UserSerializer
from users.decorators import unauthenticated_user

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@unauthenticated_user
class RegisterView(APIView):
	form = UserForm()

	def post(self,request,):
		form = UserForm(req.POST)
		if form.is_valid():
			user 		= form.save()
			username 	= form.cleaned_data.get('username')
			role		= form.cleaned_data.get('role')

			if role == 'professional':
				group = Group.objects.get(name='professionals')
			else if role == 'contributor':
				group = Group.objects.get(name='contributors')
			else:
				group = Group.objects.get(name='non-role')

			user.groups.add(group)
			
			return redirect('login')

@unauthenticated_user
class LoginView(APIView):

	def post(self,request,):
		username 	= request.data.get("username")
		password	= request.data.get("password")

		user 		= authenticate(username=username, password=password)

		if user:
			return Response({"token":user.auth_token.key})
		else:
			return Response({"error":"Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

class ListUsers(APIView):

	authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)

@login_required(login_url='login')
class UserView(viewsets.ViewSet):

	@staticmethod
	def retrieve(self, request, pk):

		queryset = User.objects.all()
		user = get_object_or_404(queryset, pk=pk)

		serialized = UserSerializer(user)
		return Response(serialized.data)

    @staticmethod
    def list(self):
        queryset        = User.objects.all()
        serialized      = UserSerializer(queryset, many=True)
        
        return Response(serialized.data)

