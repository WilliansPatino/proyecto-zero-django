from django.contrib import admin

# Register your models here.
from .models import Page





# Configuracion extra / personalizacin 
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('visible',)
    list_display = ('title', 'visible', 'created_at')
    ordering = ('-created_at',)


admin.site.register(Page, PageAdmin)

# configuracion del panel
title = "Proyecto Zero con Django"
subtitle = "Panel de gestión"

admin.site.index_title = subtitle
admin.site.site_header = title
admin.site.site_title = title