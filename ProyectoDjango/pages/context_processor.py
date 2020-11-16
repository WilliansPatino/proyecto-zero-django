from pages.models import Page

# functiones

def get_pages(request):

    pages = Page.objects.values_list('id', 'title', 'slug')

    return {
        'pages': pages
    }