from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterAPI.as_view(), name='register'),
    path('verify/', views.VerifyOTP.as_view(), name='verify'),
     path('login/', views.LoginAPI.as_view(), name='login')

]