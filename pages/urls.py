from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from pages import views

urlpatterns = patterns(
	'pages.views',
    url(r'^(?P<name>\w+)?$', views.home_page, name="Checkit"),
    url(r'^(?P<name>\w+)/submit_email/$', views.submit_email)
)