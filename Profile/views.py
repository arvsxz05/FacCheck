from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.models import User

from Profile.models import UserProfile, Report

# Create your views here.

def sign_up(request):
	if request.user.is_authenticated:
		return redirect('/')

	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		username = request.POST.get('username')
		password = request.POST.get('password')
		email = request.POST.get('email')
		user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,
                             email=email,
                             password=password)
		userP = UserProfile.objects.create(owner=user, isAdmin=False)
		return redirect('home')

	context = {
		'type': 1
	}

	return render(request, 'login.html', context = context)

def sign_in(request):
	if request.user.is_authenticated:
		return redirect('/')
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			login(request, user)
			return redirect('/')
	context = {
		'type': 2
	}
	return render(request, 'login.html', context=context)

def sign_out(request):
	logout(request)
	return redirect('signin')