from django.conf.urls import url
from django.views.defaults import page_not_found

from . import views

urlpatterns = [
	url(r'^signup/$', views.sign_up, name='signup'),
	url(r'^login/$', views.sign_in, name='signin'),
	url(r'^logout/$', views.sign_out, name='signout'),
	url(r'^validate-username/$', views.validate_username, name='validate_username'),
	url(r'^edit/(?P<username>\w+)$', views.edit_view, name='edit'),
	url(r'^view/(?P<username>\w+)$', views.view_profile, name='view'),
	url(r'^404/$', page_not_found, name="page_404"),
]