from django.shortcuts import render
from .models import News, Jobs, Documents, Blog, Articles, Questions, Answers
from ad.models import Ad
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AdSerializer
from django.shortcuts import get_object_or_404


def index(request):
    ads = Ad.objects.all()[:2]
    news = News.objects.all()
    return render(request, 'main/index.html', {'news': news, 'ads': ads})

class AdView(APIView):
    def get(self, request):
        ads = Ad.objects.all()
        serializer = AdSerializer(ads, many=True)
        return Response({"ads": serializer.data})

    def post(self, request):
        ad = request.data.get('ad')
        serializer = AdSerializer(data=ad)
        if serializer.is_valid(raise_exception=True):
            ad_saved = serializer.save()
        return Response({"success": "Ad '{}' created successfully".format(document_saved.title)})

    def put(self, request, pk):
        saved_document = get_object_or_404(Ad.objects.all(), pk=pk)
        data = request.data.get('ad')
        serializer = AdSerializer(instance=saved_ad, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            ad_saved = serializer.save()
        return Response({
            "success": "Ad '{}' updated successfully".format(document_saved.title)
        })

    def delete(self, request, pk):
        ad = get_object_or_404(Ad.objects.all(), pk=pk)
        ad.delete()
        return Response({
            "message": "Ad with id `{}` has been deleted.".format(pk)
        }, status=204)


def jobs_list(request):
    jobs = Jobs.objects.all()
    return render(request, 'main/jobs.html', {'jobs': jobs})


def documents(request):
    docs = Documents.objects.all()
    return render(request, 'main/documents.html', {'docs': docs})


def blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'main/blogs.html', {'blogs': blogs})


def articles(request, id_blog):
    articles = Articles.objects.filter(id_blog=id_blog)
    blog = Blog.objects.get(id_blog=id_blog)
    return render(request, 'main/articles.html', {'articles': articles, 'blog': blog})

def questions(request):
    questions = Questions.objects.select_related('id')
    answers = Answers.objects.select_related('id_question')
    return render(request, 'main/questions.html', {'questions': questions, 'answers': answers})