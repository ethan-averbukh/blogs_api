from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.exceptions import PermissionDenied
from ..serializers.blog import BlogSerializer
from django.shortcuts import get_object_or_404
from ..models.blog import Blog


class BlogsView(generics.CreateAPIView):
    def get(self,request):
        blogs = Blog.objects.filter(author = request.user.id)
        data = BlogSerializer(blogs, many=True).data
        return Response(data)

    def post(self,request):
        request.data['author'] = request.user.id
        blog = BlogSerializer(data=request.data)
        if blog.is_valid():
            blog.save()
            return Response(blog.data, status=status.HTTP_201_CREATED)
        else:
            return Response(blog.errors, status=status.HTTP_400_BAD_REQUEST)
    


class BlogView(generics.CreateAPIView):
    def get(self, request, pk):
        blogObject = get_object_or_404(Blog, pk=pk)
        blog = BlogSerializer(blogObject).data
        return Response(blog)
    
    def delete(self,request, pk):
        blogObject = get_object_or_404(Blog, pk=pk)
        blogObject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self,request,pk):
        blogObject = get_object_or_404(Blog, pk=pk)
        print(f"BlogObject: {blogObject}")
        blog = BlogSerializer(blogObject, data=request.data, partial=True)
        print(f"blogSerialized: {blog}")
        if request.user != blogObject.author:
            raise PermissionDenied('Unauthorized, You are not the author of this blog')
        if blog.is_valid():
            blog.save()
            return Response(blog.data)
        else:
            return Response(blog.errors, status=status.HTTP_400_BAD_REQUEST)