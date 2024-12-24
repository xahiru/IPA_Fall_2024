from django.http import HttpResponse

def helloWorld(request):
    return HttpResponse("Hello world")