from django.shortcuts import render
from .models import Ads, Credit


def index(request):
    ads = Ads.objects.all()
    return render(request, 'ad/index.html', {'ads': ads})


def detail(request, id):
    ad = Ads.objects.get(id=id)
    credit = Credit.objects.get(id_credit=ad.id_credit)
    return render(request, 'ad/detail.html', {'ad': ad, 'credit': credit, 'user': user })
