# reports/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('report', views.report_list, name='report_list'),
    path('', views.home, name='home'),
    path('dashboard', views.dash, name='dash'),
    path('login', views.loginn, name='loginn'),
    path('login/', views.loginn, name='loginn'),
    path('register', views.register, name='register'),
    path('register/', views.register, name='register'),
    path('doctor_login', views.doctor_login, name='doctor_login'),
    path('doctor_register', views.doctor_register, name='doctor_register'),
    path('docdash', views.docdash, name='docdash'),
    path('upload', views.upload_report, name='upload_report'),
    path('view/<int:pk>/', views.view_report, name='view_report'),
    path('lp/<int:pk>/', views.lp, name='lp'),
    path('mk', views.mk, name='mk'),
]
