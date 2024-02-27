from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, APIView
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404

class PostListCreateView(APIView):
     
     serializer_class = PostSerializer
     def get(self,request:Request):
        posts = Post.objects.all()
        serializer = self.serializer_class(instance=posts,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
     
     def post(self,request:Request):
        data = request.data
        serializer = self.serializer_class(data= data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.error,status=status.HTTP_400_BAD_REQUEST)
    
    
class PostRetrieveUpdateDeleteView(APIView):
    
    serializer_class = PostSerializer
    
    def get(self, request:Request, post_id: int):
        post = get_object_or_404(Post,pk = post_id) 
        serializer = self.serializer_class(post)   
        return Response(serializer.data,status=status.HTTP_200_OK) 
    
    def put(self, request:Request,post_id: int):
        post = get_object_or_404(Post,pk = post_id) 
        data = request.data
        serializer = self.serializer_class(instance = post,data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.error,status=status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self, request:Request,post_id: int):
        post = get_object_or_404(Post, pk= post_id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
        
              







 





        

    
    
    

    
         
         
     

