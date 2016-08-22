from django.conf.urls import patterns, url
from questionapi import views

urlpatterns = patterns(
	'questionapi.views',
	url(r'^questions/$', views.QuestionList.as_view(), name = 'question_list'),
	url(r'^answers/$', views.AnswersList.as_view(), name = 'answer_list'),
	url(r'^answers/(?P<qid>[0-9]+)$', views.AnswersList.as_view(), name = 'answer_list'),
	url(r'^search/$', views.Search.as_view(), name = 'search'),
	url(r'^answervote/$', views.AnswerVote.as_view(), name = 'answervote'),
	)