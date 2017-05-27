from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.views.defaults import page_not_found

from . import views

urlpatterns = [
	url(r'^signup/$', views.sign_up, name='signup'),
	url(r'^login/$', views.sign_in, name='signin'),
	url(r'^logout/$', views.sign_out, name='signout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)