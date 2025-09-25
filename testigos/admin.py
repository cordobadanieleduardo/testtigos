from django.contrib import admin
from testigos.models import *


# Register your models here.
class CandsAdmin(admin.ModelAdmin):
    model = Cands
    list_display =  ('id_ct','name_can','corporation','id_dept', 'id_mun', 'id_com',)
    search_fields = ('name_can','corporation','id_dept__name_dept','id_mun__name_mun','id_com__name_com',)  # Campos por los que puedes buscar    
    list_filter = ( 'corporation','id_dept__name_dept','id_mun__name_mun','id_com__name_com',) 
    #autocomplete_fields = ('id_dept',)

class ZonasAdmin(admin.ModelAdmin):
    model = Zonas
    readonly_fields = ('date_creacion', 'id_user')
    list_display =  ('id_t','name_table','type_witnesse','puesto',
                     'mesa', 'zona','cc','p_name',
                     's_name','p_last_name','s_last_name','email','phone',
                     'id_z_mun','id_z_dept','id_z_com','id_user'
                     )

class DivipoleAdmin(admin.ModelAdmin):
    model = Divipole
    list_display =  ('id','dd','mm','zz',
                     'pp', 'depto','municipio','nombre_puesto',
                     'total','mesas','cod_com','comuna_localidad','direccion',
                     'mesas_ocupadas',
                     )
    search_fields = ('id','nombre_puesto')

admin.site.register(Cands, CandsAdmin)
admin.site.register(Zonas, ZonasAdmin)
admin.site.register(Divipole, DivipoleAdmin)    