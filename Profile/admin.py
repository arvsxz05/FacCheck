from django.contrib import admin

from Profile.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    search_fields = ['owner__username']

admin.site.register(UserProfile, UserProfileAdmin)