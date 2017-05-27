from django.contrib import admin

from .models import Report,UserProfile

# class QuestionAdmin(admin.ModelAdmin):
# 	model = Question
# 	list_display = ('question_text', 'get_name')
# 	def get_name(self, obj):
# 		return obj.owner.first_name
admin.site.register(Report)
admin.site.register(UserProfile)