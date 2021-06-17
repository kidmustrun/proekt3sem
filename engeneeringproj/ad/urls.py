from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='ads_index'),
    path('<id_ad>', views.detail, name='ad_detail'),
    path('search/', views.search, name='search_results'),
]
