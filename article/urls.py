from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "article"

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('addarticle/', views.addArticle, name="addarticle"),
    path('article/<int:id>', views.detail, name="detail"),
    path('', views.articles, name="articles"),
]