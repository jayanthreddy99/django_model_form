from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):
    TFO = TopicModelForm()
    d = {'TFO':TFO}
    if request.method == 'POST':
        TFOD = TopicModelForm(request.POST)
        if TFOD.is_valid():
            TFOD.save()
        else:
            return HttpResponse('invalid Data!!!')
        return HttpResponse('data insert sucssessfully')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    WPFO = WebpageModelForm()
    d = {'WPFO':WPFO}
    if request.method == 'POST':
        WPFOD = WebpageModelForm(request.POST)
        if WPFOD.is_valid():
            WPFOD.save()
        else:
            return HttpResponse('invalid Data!!!')
        return HttpResponse('WPFOD data insert sucssessfully')
    return render(request,'insert_webpage.html',d)

def insert_access(request):
    ARO = AccessModelForm()
    d = {'ARO':ARO}
    if request.method == 'POST':
        AROD = AccessModelForm(request.POST)
        if AROD.is_valid():
            AROD.save()
        else:
            return HttpResponse('invalid Data!!!')
        return HttpResponse('data insert sucssessfully')
    return render(request,'insert_access.html',d)