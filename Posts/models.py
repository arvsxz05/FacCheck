import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.templatetags.static import static

def report_upload_path(instance, filename):
    return './storage/report/report_{}_{}'.format(instance.owner.username, filename)

class Report(models.Model):
	STATUS_TYPE_CHOICES = (
	    ('0', 'unattended'),
	    ('1', 'in progress'),
	    ('2', 'done'),
	)
	REPORT_TYPE_CHOICES = (
	    ('0', 'IT Equipment'),
	    ('1', 'Non-IT Equipment'),
	    ('2', 'Furnitures and Fixtures'),
	    ('3', 'Aircons'),
	    ('4', 'Lab Equipment'),
	)
	EQUIP_LOCATION_CHOICES = (
	    ('0', 'AS Bldg.'),
	    ('1', 'Undergrad Bldg.'),
	    ('2', 'Library'),
	    ('3', 'Kiosks'),
	    ('4', 'Mgt. Bldg.'),
	    ('5', 'Admin Bldg.'),
	    ('6', 'High School'),
	)
	report_type = models.CharField(max_length=1, choices=REPORT_TYPE_CHOICES)
	status_type = models.CharField(max_length=1, choices=STATUS_TYPE_CHOICES, default='0')
	owner = models.ForeignKey(User, related_name='reports', on_delete=models.CASCADE)
	description = models.TextField(max_length=200)
	pub_date = models.DateTimeField(auto_now_add=True)
	report_title = models.TextField(max_length=20)
	location = models.CharField(max_length=1, choices=EQUIP_LOCATION_CHOICES)
	pic_report = models.FileField(upload_to=report_upload_path, blank=True)

	@property
	def reportpic_url(self):
		if self.pic_report:
			return self.pic_report.url
		return static('img/unknown_thing.png')

	def __str__(self):
		return self.report_type + " : " + self.report_title