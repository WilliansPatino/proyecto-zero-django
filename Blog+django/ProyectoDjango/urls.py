"""ProyectoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""  ----- configuracion inicial   del proyecto -------------
from django.contrib import admin
from django.urls import path

from mainapp import views
from pages import views as page_views
# tambien puede utilizarse de este modo 
#               import pages.views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('inicio/', views.index, name='inicio'),
    path('pagina/<str:slug>', page_views.page, name='page')
]
"""
# Hasta aqui todo funciona; menu, estilo, paginas dinámicas y el panel de
# administracion. Ahora se utilizaran las configuracion de rutas 
# separadas por aplicacion, definidas estas en archivos y asociada con
# include()

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('', include('pages.urls'))
]


