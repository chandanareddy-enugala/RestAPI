from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, APIView
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404



@api_view(http_method_names=["GET","POST"])
def list_posts(request: Request):
    posts = Post.objects.all()
    if request.method == "POST":
        data = request.data
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.error,status=status.HTTP_400_BAD_REQUEST)
    
    serializer = PostSerializer(instance=posts,many= True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(http_method_names=["GET"])
def post_detail(request:Request, post_id:int):
     post = get_object_or_404(Post,pk = post_id)
     serializer = PostSerializer(post)
     response = {"message":"post","data":serializer.data}
     return Response(data=response,status=status.HTTP_200_OK)
 


@api_view(http_method_names=["GET", "PUT"])
def post_update(request: Request, post_id: int):
    # Fetch the post instance
    post = get_object_or_404(Post, pk=post_id)
    # If it's a GET request, just serialize and return the fetched post
    if request.method == 'GET':
        serializer = PostSerializer(instance=post)
        return Response(serializer.data)
    # If it's a PUT request, process the update
    elif request.method == 'PUT':
        data = request.data
        serializer = PostSerializer(instance=post, data=data)
        if serializer.is_valid():
            serializer.save()
            response = {"message": "Post updated successfully", "data": serializer.data}
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(http_method_names=["DELETE","GET"])
def post_delete(request: Request, post_id: int):
    post = get_object_or_404(Post, pk=post_id)
    if request.method =='GET':
        serializer = PostSerializer(instance=post)
        response= {"message": "Do you want to delete this post", "data": serializer.data}
        return Response(data = response)
    else:
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    

    
         
         
     

