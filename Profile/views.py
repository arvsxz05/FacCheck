from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import JsonResponse
from Profile.forms import UserInfoForm

from Profile.models import UserProfile
from Posts.models import Report

# Create your views here.

def sign_up(request):
	if request.user.is_authenticated:
		return redirect('/')

	context = {}
	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		username = request.POST.get('username')
		password = request.POST.get('password')
		confirm = request.POST.get('confirm')
		if password != confirm:
			context['first_name'] = first_name
			context['last_name'] = last_name
			context['username'] = username
			context['error'] = "Passwords dont match!"
			return render(request, 'login.html', context = context)

		email = request.POST.get('email')
		user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,
                             email=email,
                             password=password)
		userP = UserProfile.objects.create(owner=user, isAdmin=False)
		return redirect('home')

	context['type'] = 1;

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

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)

def edit_view (request, username):
	if not request.user.is_authenticated :
		return redirect('signin')

	if request.user.username != username :
		return redirect(reverse('page_404'))

	if request.method == 'POST':
		form = UserInfoForm(request.POST, request.FILES, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('/')  #fuhbvnjdksnhbvgfctvgybhunjhbvgfcfvgh
	else:
		form = UserInfoForm(instance=request.user)

	context = {
		'form': form,
	}
	print(request.user.profile.avatar_url)
	return render(request, 'editprofile.html', context=context)

def view_profile (request, username):
	if not request.user.is_authenticated :
		return redirect('signin')

	user_queried = get_object_or_404(User, username=username)
	context = {
		"user": user_queried,
		"reports": Report.objects.filter(owner=request.user)
	}

	return render(request, 'viewprofile.html', context=context)
