from django.conf.urls import url
from django.views.defaults import page_not_found

from . import views

urlpatterns = [
	url(r'^make-report/$', views.report, name='report'),
]