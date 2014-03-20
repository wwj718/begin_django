#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext


# Create your views here.
def hello(request):
	return HttpResponse("hello home")

def index(request):
    """
    """
    return render_to_response('index.html',{},RequestContext(request))

