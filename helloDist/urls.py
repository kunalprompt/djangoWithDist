from django.conf.urls import patterns, include, url

from views import *
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'helloDist.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', homeView),
)
urlpatterns += patterns('',
        url(r'^(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
    )