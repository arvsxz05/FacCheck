from django.contrib import admin

from Posts.models import Report

class ReportAdmin(admin.ModelAdmin):
    search_fields = ['report__id']

admin.site.register(Report, ReportAdmin)
