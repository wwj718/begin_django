#coding:utf-8

# Create your views here.
from .models import Message
from django.http import HttpResponse
from django.shortcuts import render


#from django.views.generic import list_detail
from django.shortcuts import get_object_or_404
#django.views.generic.list.ListView

def hello(request):
    return HttpResponse("Hello message")	


def message_message_list(request,template_name='message_list.html'):
    """
    Returns a news detail page.
    """
    message_list = Message.objects.all()
    return render(request, template_name, {
        'message_list': message_list,
    })
