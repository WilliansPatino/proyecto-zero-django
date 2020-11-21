from django.shortcuts import render, redirect

# 19.11.2020 
# habilita los metodos para el formulario de registro
from django.contrib.auth.forms import UserCreationForm

# 19.11
# importar el objeto para personalizar el formulario
from mainapp.forms import RegisterForm

# 19.11 // sesion flash para mensajes en formularios
from django.contrib import messages


# autenticacion de usuarios
from django.contrib.auth import authenticate, login, logout


# restringir paginas/urls
from django.contrib.auth.decorators import login_required


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

# 19.11.2020
def register_page(request):


    # validacion de la pagina de registro
    if request.user.is_authenticated:
        return redirect('inicio')
    
    else:
        
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

# 20.11.2020

def login_page(request):
    
     # validacion de la pagina de registro
    if request.user.is_authenticated:
        return redirect('inicio')
    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username,
                password=password)

            if user is not None:
                login(request, user)
                return redirect('inicio')

            else:
                messages.warning(request, 'Acceso denegado, usuario  o contraseña incorrectos')

        return render(request, 'users/login.html', {
        'title': 'Acceder'
        })

def logout_user(request):
    logout(request)
    return redirect('login')