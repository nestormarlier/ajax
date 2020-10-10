from django.contrib import admin
from core.erp.models import *

# Register your models here.

admin.site.register(Category)

class CambioMecanicoAdmin(admin.ModelAdmin):
    fields = ['create', 'parada', 'fecha_fin']
    readonly_fields = ['create']

class SetupAdmin(admin.ModelAdmin):
    fields = ['create', 'parada', 'fecha_fin']
    readonly_fields = ['create']

class ProduccionAdmin(admin.ModelAdmin):
    fields = ['create', 'parada', 'fecha_fin']
    readonly_fields = ['create']

admin.site.register(FichaTecnica)

mis_modelos = Categoria, Operario
admin.site.register(CambioMecanico, CambioMecanicoAdmin)
admin.site.register(Parada)
admin.site.register(mis_modelos)
admin.site.register(Impresora)
admin.site.register(Produccion, ProduccionAdmin)
admin.site.register(ParteImpresion)
admin.site.register(Setup, SetupAdmin)