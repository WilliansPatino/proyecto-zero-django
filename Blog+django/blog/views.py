from django.shortcuts import render, get_object_or_404

from django.core.paginator import Paginator

# Create your views here.
from blog.models import Article, Category

# restringir paginas/urls
from django.contrib.auth.decorators import login_required

# redirecciona a la pagina de log in
@login_required(login_url='login')
def list(request):

    articles = Article.objects.all()
    # 2 articulos por pagina
    paginator = Paginator(articles, 2)

    # coger numero de pagina y paginar todos los articulos
    page = request.GET.get('page')
    page_article = paginator.get_page(page)

    return render(request, 'articles/list.html', {
        'title': 'Artículos',
        'articles': page_article
	})

@login_required(login_url='login')
def category(request, category_id):

    # category = Category.objects.get(id=category_id)
    category = get_object_or_404(Category, id=category_id)

    articles = Article.objects.filter(categories=category)


    return render(request, 'categories/category.html', {
        'category': category,
        'articles': articles
    })

@login_required(login_url='login')
def article(request, article_id):

    article = get_object_or_404(Article, id=article_id)

    return render(request, 'articles/detail.html', {
        'article': article
    })