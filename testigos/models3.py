# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    t_user = models.CharField(max_length=20, blank=True, null=True)
    pass_field = models.TextField(db_column='pass', blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'admin'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Divipole(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
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

    class Meta:
        managed = False
        db_table = 'divipole'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class TCands(models.Model):
    id_ct = models.AutoField(primary_key=True)
    name_can = models.CharField(max_length=50)
    corporation = models.CharField(max_length=50)
    id_dept = models.ForeignKey('TDpts', models.DO_NOTHING, db_column='id_dept')
    id_mun = models.ForeignKey('TMuns', models.DO_NOTHING, db_column='id_mun', blank=True, null=True)
    id_com = models.ForeignKey('TComs', models.DO_NOTHING, db_column='id_com', blank=True, null=True)
    cc = models.CharField(max_length=20)
    email = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 't_cands'


class TComs(models.Model):
    id_c = models.AutoField(primary_key=True)
    name_com = models.CharField(max_length=50)
    id_mun = models.ForeignKey('TMuns', models.DO_NOTHING, db_column='id_mun')

    class Meta:
        managed = False
        db_table = 't_coms'


class TDpts(models.Model):
    id_d = models.AutoField(primary_key=True)
    cod_dep = models.CharField(max_length=50)
    name_dept = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 't_dpts'


class TMuns(models.Model):
    id_m = models.AutoField(primary_key=True)
    cod_mun = models.CharField(max_length=50)
    name_mun = models.CharField(max_length=50)
    id_dept = models.ForeignKey(TDpts, models.DO_NOTHING, db_column='id_dept')

    class Meta:
        managed = False
        db_table = 't_muns'


class TPosts(models.Model):
    id_p = models.AutoField(primary_key=True)
    cod_zona = models.CharField(max_length=50)
    cod_post = models.CharField(max_length=50)
    name_post = models.CharField(max_length=50)
    id_p_dept = models.ForeignKey(TDpts, models.DO_NOTHING, db_column='id_p_dept')
    id_p_mun = models.ForeignKey(TMuns, models.DO_NOTHING, db_column='id_p_mun')
    id_p_com = models.ForeignKey(TComs, models.DO_NOTHING, db_column='id_p_com', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_posts'


class TTables(models.Model):
    id_t = models.AutoField(primary_key=True)
    name_table = models.CharField(max_length=50)
    type_witnesse = models.CharField(max_length=25, blank=True, null=True)
    cc = models.CharField(max_length=25, blank=True, null=True)
    p_name = models.CharField(max_length=25)
    s_name = models.CharField(max_length=25, blank=True, null=True)
    p_last_name = models.CharField(max_length=25)
    s_last_name = models.CharField(max_length=25, blank=True, null=True)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    id_post = models.ForeignKey(TPosts, models.DO_NOTHING, db_column='id_post')
    save_testigos = models.IntegerField(blank=True, null=True)
    id_user = models.ForeignKey('TUser', models.DO_NOTHING, db_column='id_user')
    date_creacion = models.DateField(blank=True, null=True)
    date_export = models.DateField(blank=True, null=True)
    status_export = models.IntegerField()
    status_error = models.IntegerField(blank=True, null=True)
    desc_error = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_tables'


class TUser(models.Model):
    names_user = models.CharField(max_length=150, blank=True, null=True)
    id_candidato = models.ForeignKey(TCands, models.DO_NOTHING, db_column='id_candidato', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user'


class TZonas(models.Model):
    id_t = models.AutoField(primary_key=True)
    name_table = models.CharField(max_length=50)
    type_witnesse = models.CharField(max_length=25, blank=True, null=True)
    cc = models.CharField(max_length=25, blank=True, null=True)
    p_name = models.CharField(max_length=25)
    s_name = models.CharField(max_length=25, blank=True, null=True)
    p_last_name = models.CharField(max_length=25)
    s_last_name = models.CharField(max_length=25, blank=True, null=True)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    id_z_mun = models.ForeignKey(TMuns, models.DO_NOTHING, db_column='id_z_mun')
    id_z_dept = models.ForeignKey(TDpts, models.DO_NOTHING, db_column='id_z_dept')
    save_testigos = models.IntegerField(blank=True, null=True)
    id_user = models.IntegerField()
    date_creacion = models.DateField(blank=True, null=True)
    date_export = models.DateField(blank=True, null=True)
    status_export = models.IntegerField()
    status_error = models.IntegerField(blank=True, null=True)
    desc_error = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_zonas'
