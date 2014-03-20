#coding=utf-8
from django.conf.urls import patterns, include, url
from .views import hello,news_news_details,news_news_list
from django.shortcuts import get_object_or_404


NEWS_URL = r'(?P<id>\d+)'

urlpatterns = patterns('',
    url(r'^$',hello),
    url(r'^%s$' % NEWS_URL, news_news_details, name='news_news_details'),
    url(r'^list$' , news_news_list, name='news_news_list'),
)

