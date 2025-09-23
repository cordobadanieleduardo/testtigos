from django.contrib import admin
from testigos.models import *


# Register your models here.
class CandsAdmin(admin.ModelAdmin):
    model = Cands
    # list_display =  ('id_ct','name_can','corporation','id_dept__name_dept', 'id_mun__name_mun', 'id_com__name_com',)
    list_display =  ('id_ct','name_can','corporation','id_dept', 'id_mun', 'id_com',)
    # search_fields = ('name','location__dpto_name','location__mun_name','location__comuna_name',)  # Campos por los que puedes buscar
    # readonly_fields = ('fc', 'fm','fecha_inicio','fecha_fin')
    # list_filter = ( 'location__dpto_name','location__mun_name','location__comuna_name','mostrar',) 
    #autocomplete_fields = ('id_dept',)


admin.site.register(Cands, CandsAdmin)