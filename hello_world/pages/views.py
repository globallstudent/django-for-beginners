from django.http import HttpResponse

def home_page_view(equest):
    return HttpResponse("Hello, world!")