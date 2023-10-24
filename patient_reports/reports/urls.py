# reports/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('report', views.report_list, name='report_list'),
    path('', views.home, name='home'),
    path('login', views.loginn, name='loginn'),
    path('login/', views.loginn, name='loginn'),
    path('register', views.register, name='register'),
    path('register/', views.register, name='register'),
    path('upload', views.upload_report, name='upload_report'),
    path('view/<int:pk>/', views.view_report, name='view_report'),
    path('mk', views.mk, name='mk'),
]
