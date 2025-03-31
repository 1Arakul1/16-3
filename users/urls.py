from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('profile/', views.user_profile, name='user_profile'),
    path('logout/', views.logout, name='logout'),
]