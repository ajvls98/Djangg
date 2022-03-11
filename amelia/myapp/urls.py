from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('delete/', views.delete),
    path('read/<id>/', views.read),
]
