from django.urls import path
from mainapp import views 


urlpatterns = [
    path('', views.index, name='index'),
    path('inicio/', views.index, name='inicio'),
     path('registro/', views.register_page, name="registerpage" )
]
