from django.shortcuts import render
from .models import News, Jobs, Documents, Blog, Articles, Questions, Answers
from ad.models import Users, Ads


def index(request):
    ads = Ads.objects.all()[:2]
    news = News.objects.all()
    return render(request, 'main/index.html', {'news': news, 'ads': ads})


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