from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets,status
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Post
from rest_framework import serializers
from posts.serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

# class PostViewset(viewsets.ViewSet):
    
#     def list(self,request):
#         queryset = Post.objects.all()
#         serializer = PostSerializer(instance=queryset, many = True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
    
#     def retrieve(self,request,pk):
#         post = get_object_or_404(Post, id=pk)
#         serializer = PostSerializer(instance=post)
#         return Response(data = serializer.data, status=status.HTTP_200_OK)
    
    
# class PostViewset(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    
    