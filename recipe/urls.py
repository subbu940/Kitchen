from django.conf.urls import url
from . import views

app_name = 'recipe'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.details, name='details'),
    url(r'^save/$', views.save, name='save'),
    url(r'^(?P<res_id>[0-9]+)/$', views.display, name='display')
]

