from pages.models import Page

# functiones

def get_pages(request):

    # muestra todas las paginas
    pages = Page.objects.values_list('id', 'title', 'slug')

    # muestra las paginas filtradas con el campo visible
    pages = Page.objects.filter(visible=True).order_by('order').values_list('id', 'title', 'slug')

    return {
        'pages': pages
    }

""" o Utilizando el campo 'visible' vamos a filtrar las 
       paginas que deseamos mostrar en el menu, utilizando la funcion:

                ... objetcs.filter(visible=True)

    o  Se agrega el campo 'order' para organizar la posicion de las paginas


            .... objects.filter(...)order_by('order')

                """
        

