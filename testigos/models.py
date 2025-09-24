# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `#managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()
#from django.contrib.auth.models import AbstractUser

class Cands(models.Model):
    id_ct = models.AutoField(primary_key=True)
    name_can = models.CharField(max_length=50)
    corporation = models.CharField(max_length=50)
    id_dept = models.ForeignKey('Dpts', models.DO_NOTHING, db_column='id_dept')
    id_mun = models.ForeignKey('Muns', models.DO_NOTHING, db_column='id_mun', blank=True, null=True)
    id_com = models.ForeignKey('Coms', models.DO_NOTHING, db_column='id_com', blank=True, null=True)
    cc = models.CharField(max_length=20)
    email = models.CharField(max_length=150)

    class Meta:
        #managed = False
        db_table = 't_cands'
        verbose_name="Candidato"
        verbose_name_plural="Candidatos"
        ordering=['name_can']

    def __str__(self):
        return f"{str(self.id_ct) + ' '+ self.name_can }"


class Coms(models.Model):
    id_c = models.AutoField(primary_key=True)
    name_com = models.CharField(max_length=50)
    id_mun = models.ForeignKey('Muns', models.DO_NOTHING, db_column='id_mun')

    class Meta:
        #managed = False
        db_table = 't_coms'
        verbose_name="Comuna/Localidad"
        verbose_name_plural="Comunidades/Localidades"
                
    def __str__(self):
        return f"{str(self.name_com)}"


class Dpts(models.Model):
    id_d = models.AutoField(primary_key=True)
    cod_dep = models.CharField(max_length=50)
    name_dept = models.CharField(max_length=50)

    class Meta:
        #managed = False
        db_table = 't_dpts'
        verbose_name="Departamento"
        verbose_name_plural="Departamentos"

    def __str__(self):
        return f"{str(self.name_dept)}"


class Muns(models.Model):
    id_m = models.AutoField(primary_key=True)
    cod_mun = models.CharField(max_length=50)
    name_mun = models.CharField(max_length=50)
    id_dept = models.ForeignKey(Dpts, models.DO_NOTHING, db_column='id_dept')

    class Meta:
        #managed = False
        db_table = 't_muns'
        verbose_name="Municipio"
        verbose_name_plural="Municipios"

    def __str__(self):
        return f"{str(self.name_mun)}"


# class Posts(models.Model):
#     id_p = models.AutoField(primary_key=True)
#     cod_zona = models.CharField(max_length=50)
#     cod_post = models.CharField(max_length=50)
#     name_post = models.CharField(max_length=50)
#     id_p_dept = models.ForeignKey(Dpts, models.DO_NOTHING, db_column='id_p_dept')
#     id_p_mun = models.ForeignKey(Muns, models.DO_NOTHING, db_column='id_p_mun')
#     id_p_com = models.ForeignKey(Coms, models.DO_NOTHING, db_column='id_p_com', blank=True, null=True)

#     class Meta:
#         #managed = False
#         db_table = 't_posts'


# class Tables(models.Model):
#     id_t = models.AutoField(primary_key=True)
#     name_table = models.CharField(max_length=50)
#     type_witnesse = models.CharField(max_length=25, blank=True, null=True)
#     cc = models.CharField(max_length=25, blank=True, null=True)
#     p_name = models.CharField(max_length=25)
#     s_name = models.CharField(max_length=25, blank=True, null=True)
#     p_last_name = models.CharField(max_length=25)
#     s_last_name = models.CharField(max_length=25, blank=True, null=True)
#     email = models.CharField(max_length=150)
#     phone = models.CharField(max_length=15)
#     id_post = models.ForeignKey(Posts, models.DO_NOTHING, db_column='id_post')
#     save_testigos = models.IntegerField(blank=True, null=True)
#     id_user = models.ForeignKey('User', models.DO_NOTHING, db_column='id_user')
#     date_creacion = models.DateField(blank=True, null=True)
#     date_export = models.DateField(blank=True, null=True)
#     status_export = models.IntegerField()
#     status_error = models.IntegerField(blank=True, null=True)
#     desc_error = models.CharField(max_length=150, blank=True, null=True)

#     class Meta:
#         #managed = False
#         db_table = 't_tables'


# class User(models.Model):
# # class User(AbstractUser):
#     names_user = models.CharField(max_length=150, blank=True, null=True)
#     id_candidato = models.ForeignKey(Cands, models.DO_NOTHING, db_column='id_candidato', blank=True, null=True)

#     # username=models.CharField(max_length=12,unique=True)
#     # email=models.EmailField(max_length=120,unique=True)

#     class Meta:
#         #managed = False
#         db_table = 't_user'


class Zonas(models.Model):
    id_t = models.AutoField(primary_key=True)
    name_table = models.CharField(max_length=50)
    type_witnesse = models.CharField(max_length=25, blank=True, null=True)
    
    puesto = models.CharField(max_length=250, blank=True, null=True)
    mesa = models.CharField(max_length=250, blank=True, null=True)
    zona = models.CharField(max_length=250, blank=True, null=True)
    
    cc = models.CharField(max_length=25, blank=True, null=True)
    p_name = models.CharField(max_length=25)
    s_name = models.CharField(max_length=25, blank=True, null=True)
    p_last_name = models.CharField(max_length=25)
    s_last_name = models.CharField(max_length=25, blank=True, null=True)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    id_z_mun = models.ForeignKey(Muns, models.DO_NOTHING, db_column='id_z_mun')
    id_z_dept = models.ForeignKey(Dpts, models.DO_NOTHING, db_column='id_z_dept')
    id_z_com = models.ForeignKey(Coms, models.DO_NOTHING, db_column='id_z_com', blank=True, null=True)
    save_testigos = models.IntegerField(blank=True, null=True)
    # id_user = models.IntegerField()
    id_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, db_column='id_user')
    date_creacion = models.DateField(blank=True, null=True)
    date_export = models.DateField(blank=True, null=True)
    status_export = models.IntegerField()
    status_error = models.IntegerField(blank=True, null=True)
    desc_error = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 't_zonas'
        verbose_name="Zona"
        verbose_name_plural="Zonas"
        ordering=['type_witnesse', ]
        
    def save(self, *args, **kwargs):
        if not self.date_creacion:
            self.date_creacion = timezone.now().date()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{str(self.name_table)}"
    
    

# class Divipole(models.Model):
#     id = models.AutoField(db_column='ID',primary_key=True)
#     divipole = models.IntegerField(db_column='DIVIPOLE', blank=True, null=True, primary_key=False)  # Field name made lowercase.
#     municipio = models.IntegerField(db_column='MUNICIPIO', blank=True, null=True)  # Field name made lowercase.
#     zona = models.IntegerField(db_column='ZONA', blank=True, null=True)  # Field name made lowercase.
#     puesto = models.CharField(db_column='PUESTO', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     depto = models.CharField(db_column='DEPTO', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     municipio_nombre = models.CharField(db_column='MUNICIPIO_NOMBRE', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     nombre_puesto = models.CharField(db_column='NOMBRE_PUESTO', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     mujeres = models.IntegerField(db_column='MUJERES', blank=True, null=True)  # Field name made lowercase.
#     hombres = models.IntegerField(db_column='HOMBRES', blank=True, null=True)  # Field name made lowercase.
#     total = models.IntegerField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
#     mesas = models.IntegerField(db_column='MESAS', blank=True, null=True)  # Field name made lowercase.
#     cod_com = models.IntegerField(db_column='COD.COM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     comuna_localidad = models.CharField(db_column='COMUNA/LOCALIDAD', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     direccion = models.CharField(db_column='DIRECCION', max_length=50, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         #managed = False
#         db_table = 'divipole'



class Divipole(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dd = models.IntegerField(db_column='DD', blank=True, null=True)  # Field name made lowercase.
    mm = models.IntegerField(db_column='MM', blank=True, null=True)  # Field name made lowercase.
    zz = models.IntegerField(db_column='ZZ', blank=True, null=True)  # Field name made lowercase.
    pp = models.CharField(db_column='PP', max_length=5, blank=True, null=True)  # Field name made lowercase.
    depto = models.CharField(db_column='DEPTO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    municipio = models.CharField(db_column='MUNICIPIO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nombre_puesto = models.CharField(db_column='NOMBRE_PUESTO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mujeres = models.FloatField(db_column='MUJERES', blank=True, null=True)  # Field name made lowercase.
    hombres = models.FloatField(db_column='HOMBRES', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    mesas = models.IntegerField(db_column='MESAS', blank=True, null=True)  # Field name made lowercase.
    cod_com = models.IntegerField(db_column='COD.COM', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    comuna_localidad = models.CharField(db_column='COMUNA/LOCALIDAD', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    direccion = models.CharField(db_column='DIRECCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mesas_ocupadas = models.JSONField(db_column='MESAS_OCUPADAS',blank=True, null=True, default=list)

    class Meta:
        #managed = False
        db_table = 'divipole'
        verbose_name="Divipole"
        verbose_name_plural="Divipole"
        ordering=['id']