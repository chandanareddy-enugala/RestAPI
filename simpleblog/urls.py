
from posts.views import PostViewSet
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("",PostViewSet,basename="posts")

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('posts.urls')),
    # path("auth/",include('authentication.urls')),
    path("posts/",include(router.urls)),
    path("auth/", include("accounts.urls")),
]
