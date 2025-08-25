from django.urls import path
from . import views

urlpatterns=[
    path('posts/', views.PostView.as_view(), name = "posts"),
    path('detail/<int:pk>/', views.PostDetailView.as_view(), name = "detail"),
    path('new/', views.NewPostView.as_view(), name="new_post"),
    
]