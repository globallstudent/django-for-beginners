from django.http import HttpResponse
from django.shortcuts import render

def home_page_view(request):
    return HttpResponse("Homepage")

def about_page_view(request):
    content = {"name": "Alice"}
    return render(request, "pages/about.html", content)