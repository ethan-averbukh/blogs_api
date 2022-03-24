from ast import Pass
from xml.etree.ElementInclude import include
from django.urls import path, include
from .views import index
from .views.users import SignIn, SignOut, SignUp, PasswordChange
from .views.blogs import BlogsView, BlogView
urlpatterns = [
    path('', index.index, name='index'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-password/', PasswordChange.as_view(), name='chg-password'),
    path('blogs/', BlogsView.as_view(), name='blogs'),
    path('blogs/<int:pk>', BlogView.as_view(), name='blog')

]