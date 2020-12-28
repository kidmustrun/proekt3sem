from django.shortcuts import render
from .models import News, Jobs
from ad.models import Ads


def index(request):
    ads = Ads.objects.all()[:2]
    news = News.objects.all()
    return render(request, 'main/index.html', {'news': news, 'ads': ads})


def jobs_list(request):
    jobs = Jobs.objects.all()
    return render(request, 'main/jobs.html', {'jobs': jobs})
