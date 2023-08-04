from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('news/', views.news),
    path('recru/', views.recru),
    path('recru/<str:recru_id>/', views.recru_view, name='recru_view'),
    path('inquiry/', include('inquiry.urls')),
    path('about/', include('about.urls')),
    path('accounts/', include('accounts.urls')),
    path('recru/comment/create/<int:recru_id>/', views.recru_comment_create, name='recru_comment_create'),
    path('recru/comment/update/<int:comment_id>/', views.recru_comment_update, name='recru_comment_update'),
    path('recru/comment/delete/<int:comment_id>/', views.recru_comment_delete, name='recru_comment_delete'),


]
