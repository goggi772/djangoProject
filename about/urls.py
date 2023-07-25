from django.urls import path

from . import views

urlpatterns = [
    path('company/', views.company_intro),
    path('service/', views.service_intro),
    path('directions/', views.directions),

]
