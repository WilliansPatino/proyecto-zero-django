from blog.models import Category, Article

# functiones

def get_categories(request):

    # muestra todas las categorias, filtradas por id y asociadas a articulos
    cat_in_use = Article.objects.filter(public=True).values_list('categories', flat=True)

    categories = Category.objects.filter(id__in=cat_in_use).values_list('id', 'name')
    
    return {
        'categories': categories,
        'ids': cat_in_use
    }

