from django.http import HttpResponse

def index(request):
    return HttpResponse("Nothing Here, but server is running!")