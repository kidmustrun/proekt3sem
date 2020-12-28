from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='ads_index'),
    path('<id>', views.detail, name='ad_detail')
]
