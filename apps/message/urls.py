#coding=utf-8
from django.conf.urls import patterns, include, url
from .views import hello,message_message_list
from django.shortcuts import get_object_or_404



urlpatterns = patterns('',
    url(r'^$',hello),
    url(r'^list$' , message_message_list, name='message_message_list'),
)

