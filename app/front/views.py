# -*- coding: utf-8 -*-

from django.shortcuts import HttpResponse, render, redirect
from app.portafolio.models import Project

def home(request):
	projects = Project.objects.filter(status=True).order_by('-weight','-id')
	return render(request, 'sections/home.html', locals())

def borderlands(request):
    return redirect('http://borderlands.acarrillo.info')
