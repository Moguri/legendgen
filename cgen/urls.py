from django.conf.urls import patterns, url, include
from cgen.api import register_api


from cgen import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^(?P<cid>\d+)/$', views.detail, name='detail'),
        url(r'^new/$', views.new, name='new'),
        url(r'^(?P<cid>\d+)/delete$', views.delete, name='delete'),
        url(r'^(?P<cid>\d+)/save/$', views.save, name='save'),
        url(r'^api/', include(register_api().urls), name='api'),
)

