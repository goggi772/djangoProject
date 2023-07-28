from django.urls import path

from . import views

app_name = 'inquiry'

urlpatterns = [
    path('comments/', views.customer_comments, name='comments'),
    path('comments/<str:comments_id>/', views.comments_view, name= 'comments_view'),
    path('center/', views.customer_center),
    path('writing/', views.comments_writing, name='writing'),

]
