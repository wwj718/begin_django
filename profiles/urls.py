#coding=utf-8

from django.conf.urls import patterns, include, url
from .views import get_code
from userena import views as userena_views 
from .forms import SignupFormExtra

urlpatterns = patterns('',
	url(r'^$',userena_views.signup,{'signup_form': SignupFormExtra}),
    url(r'^get_code/$', get_code),
    url(r'^user_exist/$', get_code),

)
