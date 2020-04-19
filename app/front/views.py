# -*- coding: utf-8 -*-

from django.shortcuts import HttpResponse, render_to_response, redirect
from app.portafolio.models import Project

def home(request):
	projects = Project.objects.filter(status=True).order_by('-weight','-id')
	return render_to_response('sections/home.html', locals())

def borderlands(request):
    return redirect('http://borderlands.acarrillo.info')
