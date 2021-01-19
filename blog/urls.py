from django.urls import path
from blog.views import  About, PostDetails, CreatePost,DeletePost, UpdatePost
from blog import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', About.as_view(), name='about'),
    path('post/<int:pk>/', PostDetails.as_view(), name='details'),
    path('newpost/' ,CreatePost.as_view(), name='newpost'),
    path('delete/<int:pk>/', DeletePost.as_view(), name='delete'),
    path('update/<int:pk>/', UpdatePost.as_view(), name='update'),
]
