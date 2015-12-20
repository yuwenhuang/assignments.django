from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout #use default login/logout view

urlpatterns = [
	#url(r'^$', views.index, name='index'),
	#url(r'^index/$', views.index, name='index'),
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post_list', views.post_list, name = 'post_list'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^post/new/$', views.post_new, name='post_new'),  
	url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'), 
	# login redirect page is defined in urls.py : LOGIN_REDIRECT_URL = "/post_list/"
	url(r'^accounts/login/$',login),
    # after user log out, redirect to the index page
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    # register page
    url(r'^accounts/register/$', views.register, name = 'register'),
    #url(r'^registerok', views.registerok, name='registerok'),
]
