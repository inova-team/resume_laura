from django.contrib import admin
from django.urls import path

from landing import views

urlpatterns = [
    path('', views.renderHome, name="home"),
    path('article_list/', views.renderArticle, name="article_list"),
    path('article_detail/<int:pk>/', views.article_detail, name='article_detail'),
    path('contactanos/', views.renderContactUs_email, name="contact_us"),
]
