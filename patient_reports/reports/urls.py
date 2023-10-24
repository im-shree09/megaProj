# reports/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # path('', views.report_list, name='report_list'),
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('upload', views.upload_report, name='upload_report'),
    path('view/<int:pk>/', views.view_report, name='view_report'),
]
