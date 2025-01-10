from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# views.py
def list_articles(request):
    articles = Article.objects.all()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_articles')
    else:
        form = ArticleForm()
    context = {
        'articles': articles,
        'form': form
    }
    return render(request, 'base/list_articles.html', context)


def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_articles')
    else:
        form = ArticleForm()
    return render(request, 'base/create_article.html', {'form': form})