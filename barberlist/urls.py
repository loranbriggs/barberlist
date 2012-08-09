from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.customer_pg', name='customer_pg'),
    url(r'^employees$', 'app.views.employee_pg', name='employee_pg'),
    url(r'^archive$', 'app.views.archive', name='archive'),
    # url(r'^barberlist/', include('barberlist.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
