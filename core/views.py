from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return HttpResponse("Welcome to the Homepage!")

def about(request):
    return HttpResponse("Welcome to the about page!")