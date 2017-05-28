from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from Posts.models import Report


# @receiver(post_save)
# def create_userprofile(created, instance, **kwargs):
#     """ Create a userprofile for every new user """
#     if created:
#         UserProfile.objects.create(owner=instance)
