from django.contrib import admin

# Register your models here.
from .models import Category, Article

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'created_at', 'edited_at')

    def save_model(self, request, obj, form, change):

        if not obj.user_id:
            obj.user_id = request.user.id


        obj.save()


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)

"""  
    o   Se agrega la funcion, save_model(...) para corregir un fallo
        despues de aregar el argmento; editable=False

    

"""