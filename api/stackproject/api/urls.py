from django.conf.urls import patterns, url
from api import views

urlpatterns = patterns(
	'api.views',
	url(r'^users/$', views.UserList.as_view(), name = 'user_list'),
	url(r'^users/(?P<username>[a-zA-Z0-9._@]+)$', views.UserDetail.as_view(), name = 'user_detail'),
	url(r'^signin/$', views.LoginAuth.as_view(), name = 'sign_in'),
)