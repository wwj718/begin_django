#coding=utf-8
from django.conf.urls import patterns, include, url
from .views import hello,index

#1.6有变？
#from django.views.generic.simple import direct_to_template
from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'', hello),
    url(r'^index/$', index),

    #呈现静态“关于”页面
    (r'^about/$',  TemplateView.as_view(template_name="about.html")),
)