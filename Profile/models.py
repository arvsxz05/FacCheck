from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import admin
# Create your models here.

class UserProfile(models.Model):
	owner = models.OneToOneField(User, related_name='profile')
	isAdmin = models.BooleanField(default=False)

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
	report_type = models.CharField(max_length=1, choices=REPORT_TYPE_CHOICES)
	status_type = models.CharField(max_length=1, choices=STATUS_TYPE_CHOICES)
	owner = models.ForeignKey(User, related_name='reports')
	description = models.TextField(max_length=200)
	pub_date = models.DateTimeField(auto_now_add=True)

