from django.shortcuts import render
from .models import Ad
from django.db.models import Q
from .forms import AdForm
from django.http import HttpResponseRedirect

def index(request):
    ads = Ad.objects.all()
    count = Ad.objects.count()
    context ={}
  
    form = AdForm(request.POST or None)
    if form.is_valid():
        ad = form.save(commit=False)
        ad.author = request.user
        ad.save()

          
    context['form']= form
    context['ads']= ads
    context['count']= count
    return render(request,
        'ad/index.html',
         context
       )

def search(request):
    query = request.GET.get('q')
    object_list = Ad.objects.filter(
        Q(title__icontains=query) | Q(geo__icontains=query)
    )
    count =  object_list.count()
    return render(request, 'ad/search_results.html', {'object_list': object_list, 'query': query, 'count': count })


def detail(request, id_ad):
    context ={}

    ad = Ad.objects.get(id_ad=id_ad)
    form = AdForm(request.POST or None)

    if form.is_valid():
        ad_update = form.save(commit=False)
        ad_update.author = request.user
        ad_update.save()
  
    if request.method =="POST":
        ad.delete()
        return HttpResponseRedirect("/ads")

    context['form']= form    
    context['ad']= ad
    return render(request, 'ad/detail.html', context)
