from django.http import HttpResponse
from rest_framework import generics, status


class BlogsView(generics.CreateAPIView):
    def index(self,request):
        return HttpResponse('Hello World, you are at the blogs index')