from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('register/', views.register, name='register'),
    path('chat/<str:room_name>/', views.room, name='room'),
    # Add chat-related URLs here later
]
