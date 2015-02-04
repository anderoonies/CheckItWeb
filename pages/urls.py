from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from pages import views

urlpatterns = patterns(
	'pages.views',
<<<<<<< HEAD
    url('^(?P<name>\w+)$', views.home_page, name="Checkit"),
    url('^(?P<name>\w+)/submit_email/$', views.submit_email)
=======
    url('^$', TemplateView.as_view(template_name='index.html')),
    url(r'submit_email/$', views.submit_email)
>>>>>>> 274ff29f07d98ae71fc2e73ba9699d9bf19bf62d
)