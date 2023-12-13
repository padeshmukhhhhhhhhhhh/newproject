from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User

def index(request):
    template = loader.get_template("index.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))
def freshers_job(request):

    template = loader.get_template("news-single.html")
    
    return HttpResponse(template.render( ))


def experience_job(request):

    template = loader.get_template("experence.html")
    
    return HttpResponse(template.render( ))


def fresherplacement(request):

    template = loader.get_template("fplace.html")
    
    return HttpResponse(template.render( ))

def experienceplacement(request):

    template = loader.get_template("eplace.html")
    
    return HttpResponse(template.render( ))


def testimonial(request):

    template = loader.get_template("tens.html")
    
    return HttpResponse(template.render( ))


def campus(request):

    template = loader.get_template("campus.html")
    
    return HttpResponse(template.render( ))
def contact(request):
    template = loader.get_template("contact.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))