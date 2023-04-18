from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('Education', views.rparesumeindex),
    path('Personaldetails/<int:idx>/', views.personaldetails),
    path('Index', views.rparesumeindex),
    path('Personaldetails/<int:idx>/', views.personaldetails),
    path('', views.Dpersonaldetails,name="Index"),
    path('ProjectDetails/<int:idx>',views.ProjectDetails,name="Project")
]
