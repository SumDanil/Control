from django.urls import path
from .views import *
from comments import views

urlpatterns = [
    path('', index),
    path('test/', test),
    path('get_comments/', views.get_comments, name='get_comments'),
    path('post_comments/', views.post_comments, name='get_comments'),
]
