from django.urls import path

from .views.blogs import BlogsView

urlpatterns = [
    path('blogs/', BlogsView.as_view(), name='blogs')
]