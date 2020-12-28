from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('jobs', views.jobs_list, name='jobs'),
    path('ads', include('ad.urls'), name='ads'),
]
