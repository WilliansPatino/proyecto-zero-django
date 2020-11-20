from django.contrib import admin

# Register your models here.
from .models import Category, Article

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('name', 'created_at')
    ordering = ('-created_at',)
    search_fields = ('name','description')

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'created_at', 'edited_at')
    list_display = ('title', 'public', 'user','created_at',
    'edited_at')
    ordering = ('-created_at',)
    search_fields = ('title','public','user__username',
    'categories__name','content')
    list_filter = ('title','public','user__username',
    'categories__name')

    # guarda automaticamente el usuario
    def save_model(self, request, obj, form, change):

        if not obj.user_id:
            obj.user_id = request.user.id

        obj.save()


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)

"""  
    o   Se agrega la funcion, save_model(...) para corregir un fallo
        despues de aregar el argmento; editable=False

    o   Parametros que puede usarse para personalizar el
        panel de administracion, aqui ejemplos:


        readonly_fields = ('created_at', 'updated_at')
        search_fields = ('title', 'content')
        list_filter = ('visible',)
        list_display = ('title', 'visible', 'created_at')
        ordering = ('-created_at',)

"""