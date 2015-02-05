from django.conf.urls import patterns, include, url
from django.contrib import admin
import pages.urls
import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'landingpage.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(pages.urls))
)

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )