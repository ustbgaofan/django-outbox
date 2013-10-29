from django.conf.urls import patterns, include, url

from outbox.views import OutboxTemplateView, MailTemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_outbox.views.home', name='home'),
    # url(r'^django_outbox/', include('django_outbox.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^outbox/$', OutboxTemplateView.as_view(), name='outbox'),
    url(r'^outbox/(?P<id>.+)/$', MailTemplateView.as_view(), name='mail'),
)
