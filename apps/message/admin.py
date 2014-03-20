#coding:utf-8
from django.contrib import admin
#from django.contrib.markup.templatetags.markup import restructuredtext

from .models import Message

#from django_admin_bootstrapped.widgets import GenericContentTypeSelect

    
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name','email','content', 'create_time')

admin.site.register(Message, MessageAdmin)


