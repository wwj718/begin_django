#coding:utf-8
from django.contrib import admin
#from django.contrib.markup.templatetags.markup import restructuredtext

from .models import News,NewsCategory

#from django_admin_bootstrapped.widgets import GenericContentTypeSelect



    
class NewsAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    fields = ('order','category', 'title', 'content_html','content_pic' )
    list_display = ('order','category', 'title', 'view_times', 'create_time')
    ordering = ('-create_time', )
    #save_on_top = True


    # def save_model(self, request, obj, form, change):
    #     #obj.author = request.user
    #     if not obj.summary:
    #          obj.summary = obj.content_html
    #     # if not obj.is_old:
    #     #     obj.content_html = restructuredtext(obj.content)
    #     else:
    #         obj.content_html = obj.content_html.replace('\r\n', '<br/>')
    #         import re
    #         obj.content_html = re.sub(r"\[cc lang='\w+?'\]", '<pre>', obj.content_html)
    #         obj.content_html = obj.content_html.replace('[/cc]', '</pre>')
    #     obj.save()


class NewsCategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name','create_time')



admin.site.register(News, NewsAdmin)
admin.site.register(NewsCategory, NewsCategoryAdmin)


