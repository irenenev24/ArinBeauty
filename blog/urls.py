from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('sustainability/', views.sustainability, name='sustainability'),
    path('<slug:category_slug>/<slug:slug>/', views.detail, name='post_detail'),
    path('<slug:slug>', views.category, name='category_detail'),
    path('add_post/', views.add_post, name='add_post'),
    path('edit/<slug:slug>/', views.edit_post, name='edit_post'),
    path('delete/<slug:slug>/', views.delete_post, name='delete_post'),
]
