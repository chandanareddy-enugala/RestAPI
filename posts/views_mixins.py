from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status,generics,mixins
from rest_framework.decorators import api_view, APIView
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404

class PostListCreateView(generics.GenericAPIView,
                         mixins.ListModelMixin,
                         mixins.CreateModelMixin):
     
     serializer_class = PostSerializer
     queryset = Post.objects.all()
     
     def get(self, request:Request):
         return self.list(request)
         
     def post(self, request:Request):
         return self.create(request)
        
          
    
class PostRetrieveUpdateDeleteView(generics.GenericAPIView,
                                   mixins.RetrieveModelMixin,
                                   mixins.UpdateModelMixin,
                                   mixins.DestroyModelMixin):
    
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
    def get(self, request:Request,pk):
        return self.retrieve(request)
        
    
    def put(self, request:Request,pk: int):
        return self.update(request)
        
          
    def delete(self, request:Request,pk: int):
        return self.destroy(request)
        
        
        
              







