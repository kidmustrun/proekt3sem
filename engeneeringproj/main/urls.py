from django.urls import path, include
from . import views
from .views import (
    AdView
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('jobs/', views.jobs_list, name='jobs'),
    path('ads/', include('ad.urls'), name='ads'),
    path('documents/', views.documents, name='documents'),
    path('api/ads/', AdView.as_view(), name="ads_api"),
    path('api/ads/<int:pk>', AdView.as_view()),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/<id_blog>', views.articles, name='blog_articles'),
    path('questions/', views.questions, name='questions'),
    path('dashboard/', include('dashboard.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

