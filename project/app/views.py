from django.shortcuts import render,redirect 
from django.http import HttpRequest, HttpResponse
from .models import project

# Create your views here.
projectObject=project(title="",description="",image="",vedio="")
projectObject.save()

def aboutMe(request:HttpRequest):
     projectObject=project.objects.all()
     return render(request,"app/aboutMe.html")

def hello(request:HttpRequest):
     projectObject=project.objects.all()
     return render(request,"app/hello.html",{"projectObject":projectObject})


def index(request:HttpRequest):
     projectObject=project.objects.all()
     return render(request,"app/index.html",{"projectObject":projectObject })

def SitesDesign(request:HttpRequest):
     projectObject=project.objects.all()
     return render(request,"app/SitesDesign.html")

def sports(request:HttpRequest):
     projectObject=project.objects.all()
     return render(request,"app/sports.html")

def TryToBeCalm(request:HttpRequest):
     projectObject=project.objects.all()
     return render(request,"app/TryToBeCalm.html")

     