from django.shortcuts import render

# restringir paginas/urls
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Page

@login_required(login_url='login')
def page(request, slug):

    page = Page.objects.get(slug=slug)

    return render(request, 'pages/page.html', {
        'page': page
    })