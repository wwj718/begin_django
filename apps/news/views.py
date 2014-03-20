#coding:utf-8

# Create your views here.
from .models import News
from django.http import HttpResponse
from django.shortcuts import render


#from django.views.generic import list_detail
from django.shortcuts import get_object_or_404
#django.views.generic.list.ListView

def hello(request):
    return HttpResponse("Hello news")	

def news_news_details(request,id,template_name='news_details.html'):
    """
    Returns a news list page.
    """
    news = get_object_or_404(News, id=int(id))
    return render(request, template_name, {
        'news': news,
    })


def news_news_list(request,template_name='news_list.html'):
    """
    Returns a news detail page.
    """
    news_list = News.objects.all()
    return render(request, template_name, {
        'news_list': news_list,
    })
