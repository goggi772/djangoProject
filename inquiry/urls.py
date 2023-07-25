from django.urls import path

from . import views

app_name = 'inquiry'

urlpatterns = [
    path('comments/', views.customer_comments, name='comments'),
    path('center/', views.customer_center),
    path('writing/', views.comments_writing, name='writing'),

]
