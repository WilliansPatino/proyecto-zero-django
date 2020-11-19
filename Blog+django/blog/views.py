from django.shortcuts import render, get_object_or_404

# Create your views here.
from blog.models import Article, Category


def list(request):

    articles = Article.objects.all()

    return render(request, 'articles/list.html', {
        'title': 'Artículos',
        'articles': articles
	})

def category(request, category_id):

    # category = Category.objects.get(id=category_id)
    category = get_object_or_404(Category, id=category_id)

    articles = Article.objects.filter(categories=category)


    return render(request, 'categories/category.html', {
        'category': category,
        'articles': articles
    })