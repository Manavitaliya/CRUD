from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_redirect, name='home'),
    path('students/', views.student_list, name='student_list'),
    path('create/', views.student_create, name='student_create'),
    path('update/<int:pk>/', views.student_update, name='student_update'),
    path('delete/<int:pk>/', views.student_delete, name='student_delete'),
]