from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View


# displaying the Function base views

def Fbvstring(request):
    return HttpResponse('<h1>this is Function Base View <h1>')


def fbv_html(request):
    return render(request,'fbvstring.html')


# displaying The Class Base Views

class Cbvstring(View):
    def get(self,request):
        return HttpResponse('<h1>This is Class base View </h1>')


# Rendering the data from Class base Views in html page

class Cbvtemp(View):
    def get(self,request):
        return render(request,'Cbv_first.html')