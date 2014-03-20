#coding:utf-8

from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
#edit by wwj
from django.contrib import admin
admin.autodiscover()

# import xadmin
# xadmin.autodiscover()

#注册插件
# from xadmin.plugins import xversion
# xversion.register_models() 
#end wwj

urlpatterns = patterns('',

    #静态页，直达
    url(r'^about/$', TemplateView.as_view(template_name="about.html")),
    
    #edit by wwj
    #url(r'^grappelli/', include('grappelli.urls')),
    url(r'^home/', include("apps.home.urls")),
    url(r'^news/', include("apps.news.urls")),
    url(r'^message/', include("apps.message.urls")),

    url(r'^admin/', include(admin.site.urls)),

    #(r'^grappelli/', include('grappelli.urls')),
    #(r'^filebrowser/',include('filebrowser.urls')),
    #url(r'^xadmin/', include(xadmin.site.urls)),
                       
    url(r'^ueditor/',include('DjangoUeditor.urls' )),#for ueditor
    #end wwj

)
urlpatterns += staticfiles_urlpatterns()

#edit wwj to use media
from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#end wwj
