from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

urlpatterns=[
    path('signup/', views.SignUp.as_view(), name="signup"),
    path('pass_change/', PasswordChangeView.as_view(template_name="registration/password_change.html"), name="password_change"),
    path('pass_change/done/', PasswordChangeDoneView.as_view(template_name="registration/password_change_done.html"), name="password_change_done"),
]