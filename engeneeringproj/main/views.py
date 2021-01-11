from django.shortcuts import render
from .models import News, Jobs, Documents, Blog, Articles, Questions, Answers
from ad.models import Users, Ads
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import DocumentSerializer
from django.shortcuts import get_object_or_404


def index(request):
    ads = Ads.objects.all()[:2]
    news = News.objects.all()
    return render(request, 'main/index.html', {'news': news, 'ads': ads})

class DocumentView(APIView):
    def get(self, request):
        documents = Documents.objects.all()
        serializer = DocumentSerializer(documents, many=True)
        return Response({"documents": serializer.data})

    def post(self, request):
        document = request.data.get('document')
        serializer = DocumentSerializer(data=document)
        if serializer.is_valid(raise_exception=True):
            document_saved = serializer.save()
        return Response({"success": "Document '{}' created successfully".format(document_saved.title)})

    def put(self, request, pk):
        saved_document = get_object_or_404(Documents.objects.all(), pk=pk)
        data = request.data.get('document')
        serializer = DocumentSerializer(instance=saved_document, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            document_saved = serializer.save()
        return Response({
            "success": "Document '{}' updated successfully".format(document_saved.title)
        })

    def delete(self, request, pk):
        # Get object with this pk
        document = get_object_or_404(Documents.objects.all(), pk=pk)
        document.delete()
        return Response({
            "message": "Document with id `{}` has been deleted.".format(pk)
        }, status=204)


def jobs_list(request):
    jobs = Jobs.objects.all()
    return render(request, 'main/jobs.html', {'jobs': jobs})


def documents(request):
    docs = Documents.objects.all()
    return render(request, 'main/documents.html', {'docs': docs})


def blogs(request):
    blogs = Blog.objects.select_related('id_user')
    return render(request, 'main/blogs.html', {'blogs': blogs})


def articles(request, id):
    articles = Articles.objects.filter(id_blog=id)
    blog = Blog.objects.get(id=id)
    return render(request, 'main/articles.html', {'articles': articles, 'blog': blog})

def questions(request):
    questions = Questions.objects.select_related('id_user')
    answers = Answers.objects.select_related('id_question')
    return render(request, 'main/questions.html', {'questions': questions, 'answers': answers})