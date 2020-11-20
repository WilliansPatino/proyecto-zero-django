from django.shortcuts import render, redirect

# 19.10.2020 
# habilita los metodos para el formulario de registro
from django.contrib.auth.forms import UserCreationForm

# 19.10
# importar el objeto para personalizar el formulario
from mainapp.forms import RegisterForm

# 19.10 // sesion flash para mensajes en formularios
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'mainapp/index.html', {
        'title':'Inicio'
    }
    )

def about(request):

    return render(request, 'mainapp/about.html', {
        'title':'Sobre el autor'   }
    )

# 19.10.2020
def register_page(request):

    # formulario original django
    #----register_form = UserCreationForm()
    # desabilitado el formulario original para utilizar
    # un nuevo formulario personalizado
    register_form = RegisterForm()


    if request.method == 'POST':
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Registrado con éxito')

            return redirect('inicio')


    return render(request, 'users/register.html', {
        'title': 'Registro',
        'register_form': register_form
         }
    )