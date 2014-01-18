from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^rest/v1/sessions/docs/', include('rest_framework_swagger.urls')),
    url(r'^rest/v1/sessions', include('rememerme.sessions.rest.urls'))
)
