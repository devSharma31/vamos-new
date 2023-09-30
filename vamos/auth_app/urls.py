from django.contrib import admin
from django.urls import path
from . import views

app_name = 'auth_app'

urlpatterns = [
    path('index/', views.index, name='Home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('activate/<email_token>/' , views.email_verification , name="email_verification"),
    path('password_reset/', views.password_reset, name='password_reset'),
    # Add more URL patterns here
]
