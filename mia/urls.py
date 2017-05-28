from django.conf.urls import url
from . import views

app_name = 'mia'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^experience/$', views.experience, name='experience'),
	url(r'^interests$', views.interests, name='interests'),
	url(r'^publications$', views.publications, name='publications'),
]