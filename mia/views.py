# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
	return render(request,'mia/index.html')

def experience(request):
	return render(request,'mia/experience.html')

def publications(request):
	return render(request,'mia/publications.html')

def interests(request):
	return render(request,'mia/interests.html')