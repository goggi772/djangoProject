from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('news/', views.news),
    path('recru/', views.recru),
    path('recru/<str:id>/', views.recru_view),
    path('inquiry/', include('inquiry.urls')),
    path('about/', include('about.urls')),
    path('login/', views.login)

]
