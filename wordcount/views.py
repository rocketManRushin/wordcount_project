from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, "home.html")

def count(request):
    fulltext = request.GET["fulltext"]

    words = fulltext.split()

    return render(request, "count.html", {"fulltext": fulltext, "count": len(words)})

def about(request):
    return render(request, "about.html")