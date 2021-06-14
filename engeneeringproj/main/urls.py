from django.urls import path, include
from . import views
from .views import (
    DocumentView
)

urlpatterns = [
    path('', views.index, name='home'),
    path('jobs/', views.jobs_list, name='jobs'),
    path('ads/', include('ad.urls'), name='ads'),
    path('documents/', views.documents, name='documents'),
    path('api/documents/', DocumentView.as_view()),
    path('api/documents/<int:pk>', DocumentView.as_view()),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/<id>', views.articles, name='blog_articles'),
    path('questions/', views.questions, name='questions'),
    path('dashboard/', include('dashboard.urls')),
]
