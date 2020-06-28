import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.templatetags.static import static

def avatar_upload_path(instance, filename):
    return './storage/user/user_{}_{}'.format(instance.owner.username, filename)

class UserProfile(models.Model):
	owner = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
	isAdmin = models.BooleanField(default=False)
	avatar = models.FileField(upload_to=avatar_upload_path, blank=True)

	@property
	def avatar_url(self):
		if self.avatar:
			return self.avatar.url
		return static('img/unknown.jpg')

	def __str__(self):
		return self.owner.username