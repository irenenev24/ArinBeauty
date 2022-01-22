from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('<slug:slug>/', views.detail, name='detail'),
    path('sustainability/', views.sustainability, name='sustainability'),
    path('category/<slug:slug>/', views.category, name='category'),
]
