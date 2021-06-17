from django.shortcuts import render
from .models import Ad, Credit
from django.db.models import Q

def index(request):
    ads = Ad.objects.all()
    count = Ad.objects.count()
    return render(request, 'ad/index.html', {'ads': ads, 'count': count})

def search(request):
    query = request.GET.get('q')
    object_list = Ad.objects.filter(
        Q(title__icontains=query) | Q(geo__icontains=query)
    )
    count =  object_list.count()
    return render(request, 'ad/search_results.html', {'object_list': object_list, 'query': query, 'count': count })

def detail(request, id_ad):
    ad = Ad.objects.get(id_ad=id_ad)
    credit = Credit.objects.get(id_credit=ad.id_credit)
<<<<<<< HEAD
    return render(request, 'ad/detail.html', {'ad': ad, 'credit': credit, 'user': user })
=======
    return render(request, 'ad/detail.html', {'ad': ad, 'credit': credit })
>>>>>>> 70ea69988d621a420545d593324f0e77d8b98749
