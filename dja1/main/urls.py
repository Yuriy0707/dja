from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='about'),
    path('', views.index2, name='home')
]
