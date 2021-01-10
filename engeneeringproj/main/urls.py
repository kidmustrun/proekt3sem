from django.urls import path, include
from . import views
from .views import (
    NewUpdate,
    NewDelete
)

urlpatterns = [
    path('', views.index, name='home'),
    path('create_new/', views.createNew),
    path('edit_new/<int:pk>/', NewUpdate.as_view(), name='new_edit'),
    path('post/<int:pk>/delete/', NewDelete.as_view(), name='new_delete'),
    path('jobs/', views.jobs_list, name='jobs'),
    path('ads/', include('ad.urls'), name='ads'),
    path('documents/', views.documents, name='documents'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/<id>', views.articles, name='blog_articles'),
    path('questions', views.questions, name='questions')
]
