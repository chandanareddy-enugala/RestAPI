from . import views
from django.urls import path
from  .views_mixins import PostListCreateView,PostRetrieveUpdateDeleteView
from .function_based_views import post_detail,post_update,post_delete
#from . class_based_views import PostListCreateView, PostRetrieveUpdateDeleteView
urlpatterns = [
    
    #path("homepage/",homepage, name ="posts_home"),
    path('listpage/',PostListCreateView.as_view(),name ="list_posts"),
    path('listupdatedelete/<int:pk>',PostRetrieveUpdateDeleteView.as_view(),name ="list_update_delete"),
    path('listpage/<int:post_id>',post_detail,name ="post_detail"),
    path('listupdate/<int:post_id>',post_update,name ="post_update"),
    path('listdelete/<int:post_id>',post_delete,name ="post_delete")
]
