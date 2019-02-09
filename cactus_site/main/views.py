# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response

# Create your views here.
def main(request):
    request.encoding = 'utf8'
    return render(request, 'index.html')

def news(request):
    request.encoding = 'utf-8'
    return render(request , 'news.html')

def about(request):
    request.encoding = 'utf-8'
    return render(request , 'about.html')

def attributes(request):
    request.encoding = 'utf-8'
    return render(request , 'attributes.html')

def books(request):
    request.encoding = 'utf-8'
    return render(request , 'books.html')

def catalogue(request):
    request.encoding = 'utf-8'
    return render(request, 'catalogue.html')

def club_member(request):
    request.encoding = 'utf-8'
    return render(request, 'club_member.html')

def passage(request):
    request.encoding = 'utf-8'
    return render(request, 'passage.html')

def count_member(request):
    request.encoding = 'utf-8'
    return render(request, 'count_member.html')