from django.shortcuts import render
from .models import Article

def list_articles(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'base/list_articles.html', context)
