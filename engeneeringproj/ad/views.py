from django.shortcuts import render
from .models import Ads


def index(request):
    ads = Ads.objects.all()
    return render(request, 'ad/index.html', {'ads': ads})


def detail(request, id):
    ad = Ads.objects.get(id=id)
    return render(request, 'ad/detail.html', {'ad': ad})
