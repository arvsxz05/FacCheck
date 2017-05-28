from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
# from django.core.files import File
# import urllib
# from Posts.forms import ReportForm
from Posts.models import Report

def report(request):
	if not request.user.is_authenticated:
		return redirect('/')
	context = {
		'eq_type': Report.REPORT_TYPE_CHOICES,
		'location': Report.EQUIP_LOCATION_CHOICES,
	}

	if request.method == "POST":
		report_title = request.POST.get('report_title')
		description = request.POST.get('description')
		report_type = request.POST.get('report_type')
		location = request.POST.get('location')
		img_report = request.FILES.get('img_report')
	# 	form = ReportForm(request.POST, request.FILES, instance=request.user)

	# 	if form.is_valid():
	# 		form.save()
	# 		return redirect('/')
	# else:
	# 	 form = ReportForm()

	# context = {
	# 	'form': form
	# }
    # return render(request, 'registration/edit_profile.html', context=context)

		# result = urllib.urlretrieve(request.POST.get('img_report'))

		# print(File(open(result[0])));

		# print(request.POST.get('img_report'))

		if not (report_title or description or report_type or location or img_report) :
			context['error'] = "Empty fields are not allowed"
			return render(request, 'submit_report.html', context=context)

		Report.objects.create(report_title=report_title, description=description, 
			report_type=report_type, owner=request.user, location=location, pic_report=img_report)

	return render(request, 'submit_report.html', context=context)