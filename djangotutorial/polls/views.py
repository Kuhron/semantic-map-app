from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello world")


def asdf(request):
    response_content = "<p>" + "asdf "*1000 + "</p>"
    return HttpResponse(response_content)
