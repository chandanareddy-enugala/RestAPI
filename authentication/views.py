from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view,permission_classes
from rest_framework_simplejwt.tokens import RefreshToken 
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import(
    Userserializer,
    PasswordChangeSerializer,
    PasswordResetSerializer
)
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator

user = get_user_model()


@api_view(http_method_names=["POST"])
#@permission_classes([permissions.AllowAny])
def user_create(request):
    serializer = Userserializer(data=request.data)
    if serializer.is_valid():
        if user := serializer.save():
            json = serializer.data
            refresh = RefreshToken.for_user(user)
            json["refresh"] = str(refresh)
            json["access"] = str(refresh.access_token)
            return Response(json,status=201)
        return Response(serializer.errors, status=400)