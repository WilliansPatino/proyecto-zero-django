from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField

""" para asociar los usuarios del framework django """
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100,
    verbose_name='Nombre')
    description = models.CharField(max_length=255, 
    verbose_name='Descripción')
    created_at = models.DateTimeField(auto_now_add=True,
    verbose_name='Creado el')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categoría'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=150,
    verbose_name='Título')
    content = RichTextField(verbose_name='Contenido')
    image = models.ImageField(default='null',
    verbose_name='Imagen')
    public = models.BooleanField(verbose_name='¿Publicado?')
    user = models.ForeignKey(User, editable=False, verbose_name='Usuario',
    on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, 
    verbose_name='Categorías', blank=True)
    created_at = models.DateTimeField(auto_now_add=True,
    verbose_name='Creado el')
    edited_at = models.DateTimeField(auto_now=True,
    verbose_name='Editado el')

    class Meta:
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'

    def __str__(self):
        return self.title

"""  NOTAS 

    o   on_delete=models.CASCADE
        
        Este parametro, causa que al eliminar el usuario, se borraran
        los articulos vinculados al usuario.
        Si se borrar un usuario, todos los articulo seran removidos.

    o  models.ManyToManyField
        se establece una relacion de Muchos a Muchos

    o  Para evitar que el usuario sea elegido o cambiado a otro.

            se agrega, editable=False

        user .... models.ForeignKey(User, editable=False, ...)

"""