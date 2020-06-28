from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from Posts.models import Report


def home(request):
	if not request.user.is_authenticated:
		return redirect('signin')

	unattended = []
	in_progress = []
	done = []

	temp = Report.objects.filter(status_type='0').order_by('-pub_date')
	for x in zip(*[iter(temp)]*2):
		unattended.append(x)
	if len(temp)%2 == 1 :
		unattended.append((temp[len(temp)-1], None))
	temp = Report.objects.filter(status_type='1').order_by('-pub_date')
	for x in zip(*[iter(temp)]*2):
		in_progress.append(x)
	if len(temp)%2 == 1 :
		in_progress.append((temp[len(temp)-1], None))
	temp = Report.objects.filter(status_type='2').order_by('-pub_date')
	for x in zip(*[iter(temp)]*2):
		done.append(x)
	if len(temp)%2 == 1 :
		done.append((temp[len(temp)-1], None))

	context = {
		'unattended': unattended,
		'in_progress': in_progress,
		'done': done,
	}
	return render(request, 'homepage.html', context=context)
