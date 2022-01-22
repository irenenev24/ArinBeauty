from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<slug:slug>/', views.detail, name='detail'),
    path('category/<slug:slug>/', views.category, name='category'),
]
