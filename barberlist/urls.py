from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from app.views import get_names, get_employ, add_name, add_employ, archive
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.get_names', name='get_names'),
    url(r'^$', 'app.views.add_name', name='add_name'),
    url(r'^employees$', 'app.views.get_employ', name='get_employ'),
    url(r'^employees$', 'app.views.add_employ', name='add_employ'),
    url(r'^archive$', 'app.views.archive', name='archive'),
    # url(r'^barberlist/', include('barberlist.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
