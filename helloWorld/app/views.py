from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. Just trying CICD.")