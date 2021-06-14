from django.shortcuts import render
from .models import Ad, Credit


def index(request):
    ads = Ad.objects.all()
    count = Ad.objects.count()
    return render(request, 'ad/index.html', {'ads': ads, 'count': count})


def detail(request, id_ad):
    ad = Ad.objects.get(id_ad=id_ad)
    credit = Credit.objects.get(id_credit=ad.id_credit)
    return render(request, 'ad/detail.html', {'ad': ad, 'credit': credit })
