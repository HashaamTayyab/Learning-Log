"""Defining URL patterns for learning_logs app."""
from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home Page
    path('', views.index, name = 'index'),
    # Page that shows all the topics.
    path('topics/', views.topics, name = 'topics'),
    path('topics/<int:topic_id>', views.topic, name = 'topic'),
]