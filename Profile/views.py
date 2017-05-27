from django.shortcuts import render

# Create your views here.

def sign_up(request):
	if request.method == 'POST':
		print "sign_up"
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		username = request.POST.get('username')
		password = request.POST.get('password')
		email = request.POST.get('email')
		print first_name," ",last_name
		user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,
                             email=email,
                             password=password)
		userP = UserProfile.objects.create(owner=user)
