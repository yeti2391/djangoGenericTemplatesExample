from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('courses/', views.CourseView.as_view(), name='courses'),
]
