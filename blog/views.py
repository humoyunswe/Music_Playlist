from django.shortcuts import render
from django.http import HttpResponse

import json

# Create your views here.

import os

os.chdir(os.getcwd() + '/blog')
def home(request):
    file = open('tracks.json', 'r')
    data = json.load(file)
    cnt = len(data)

    return render(request, 'blog/index.html', context={'data':data,'cnt':cnt})


