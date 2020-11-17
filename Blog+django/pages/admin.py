from django.contrib import admin

# Register your models here.
from .models import Page


admin.site.register(Page)

# configuracion del panel
title = "Proyecto Zero con Django"
subtitle = "Panel de gestión"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle


""" moestrar fechas; creado/editado """
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')