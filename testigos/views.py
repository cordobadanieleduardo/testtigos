from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic

from django.contrib.auth import authenticate, login

from django.shortcuts import redirect, render


# from django.contrib.auth.tokens import default_token_generator
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes
# from django.conf import settings
from django.urls import reverse_lazy #, reverse
# from django.template.loader import render_to_string
# from django.core.mail import EmailMultiAlternatives
from django.http import JsonResponse
#from django.shortcuts import redirect, render
from django.db.models import Count
from django.contrib.auth.models import User as usuario_sistema
from .models import *


class MixinFormInvalid:
    def form_invalid(self,form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

class SinPrivilegios(LoginRequiredMixin, PermissionRequiredMixin, MixinFormInvalid):
   # login_url = 'testigos:login'
    raise_exception=False
    redirect_field_name="redirecto_to"

    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user==AnonymousUser():
            self.login_url='testigos:sin_privilegios'
        return HttpResponseRedirect(reverse_lazy(self.login_url))
    
# class Home(LoginRequiredMixin, generic.TemplateView):
class Home( generic.TemplateView):
    template_name = 'login/index.html'
    #login_url='testigos:home'
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     #context["departamentos"] = Dpts.objects.all().order_by('name_dept')                
    #     return context

def getCandidato(request):
    try:
        candidato = Cands.objects.filter(email = request.user.email).first()
    except Cands.DoesNotExist:
        candidato = None
    print('candidato',candidato)
    return candidato

def cargar_departamentos(request):
    corp = request.GET.get('corporacion')
    if corp == 'CMJ':
        departamentos = Dpts.objects.all().exclude(id_d__in=[10]).order_by('name_dept')
    else:
        #departamentos = Dpts.objects.all().exclude(id_d__in=[2,3,13,21]).order_by('name_dept')
        departamentos = Dpts.objects.all().exclude(id_d__in=[1,4,5,6,7,8,9,11,12,14,15,16,17,18,19,20,22,23,24,25,26,27,28,29,30,31,32,33]).order_by('name_dept')
        
    return JsonResponse(list(departamentos.values('id_d', 'name_dept')), safe=False) 

def cargar_municipios(request):
    dept_id = request.GET.get('departamento')
    municipios = Muns.objects.filter(id_dept=dept_id).order_by('name_mun')
    return JsonResponse(list(municipios.values('id_m', 'name_mun')), safe=False) 

def cargar_comunas(request):
    mun_id = request.GET.get('mun')
    comunas = Coms.objects.filter(id_mun=mun_id).order_by('id_c', 'name_com')
    return JsonResponse(list(comunas.values('id_c', 'name_com')), safe=False) 

def cargar_zonas(request):
    candidato:Cands = getCandidato(request)    
    if (candidato.id_dept and candidato.id_mun ):    
        puestos = Divipole.objects\
                    .filter(dd=candidato.id_dept,mm=candidato.id_mun)\
                    .values('zz', 'zz')\
                    .order_by('zz')        
    return JsonResponse(list(puestos), safe=False) 

def cargar_puestos(request):
    candidato:Cands = getCandidato(request)  
    zz:int = int(request.GET.get('zz',0)) 
    if (candidato.id_dept and candidato.id_mun and zz>0 ):    
        puestos = Divipole.objects\
                    .filter(dd=candidato.id_dept.cod_dep,mm=candidato.id_mun.cod_mun,zz=zz)\
                    .values('id', 'nombre_puesto')\
                    .order_by('nombre_puesto')
        return JsonResponse(list(puestos), safe=False) 
    else:                      
        return JsonResponse(list(), safe=False)

def cargar_mesas(request):
    mesas=None
    puesto_id = request.GET.get('puesto_id',None)
    candidato:Cands = getCandidato(request)
    if(puesto_id):        
        mesas = Divipole.objects\
            .filter(id=puesto_id)\
            .values('id', 'mesas','mesas_ocupadas')\
            .order_by('nombre_puesto')
    elif candidato.id_dept and candidato.id_mun and puesto_id:
        mesas = Divipole.objects\
            .filter(dd=candidato.id_dept.cod_dep,mm=candidato.id_mun.cod_mun, id=puesto_id)\
            .values('id', 'mesas','mesas_ocupadas')\
            .order_by('nombre_puesto')
    
    print('mesas * ', mesas)
    num=0
    mesas_ocupadas= []
    if mesas:
        num =mesas[0]['mesas']
        mesas_ocupadas = list(mesas[0]['mesas_ocupadas']) if mesas[0]['mesas_ocupadas'] else []
    if num >0:    
        # mi_lista = [i for i in range(1, num)]    
        mi_lista = []
        for i in range(num):
            if (i+1) not in mesas_ocupadas:                
                mi_lista.append({'id':int(i+1) , 'nombre_mesa':'Mesa '+str(i+1)})
        return JsonResponse((mi_lista), safe=False) 
    else:
        return JsonResponse(list(), safe=False) 

def cargar_candidatos(request):
    corp = request.GET.get('corp', None)
    dept_id = request.GET.get('dep',0)
    mun_id = request.GET.get('mun',0)
    com_id = request.GET.get('com',0)
    candidatos = None
    
    corp = corp if str(corp) else None
    dept_id = int(dept_id) if dept_id else None
    mun_id = int(mun_id) if mun_id else None
    com_id = int(com_id) if com_id else None

    
    print('corp',corp)
    print('dept_id',dept_id)
    print('mun_id', mun_id)
    print('com_id',com_id)
    
    # if corp == "ALCALDE" or corp=="CONCEJO":        
    #     candidatos = Cands.objects.filter(corporation=corp, id_dept=dept_id, id_mun=mun_id ).order_by('name_can')
    # elif corp=="ASAMBLEA" or corp=="GOBERNADOR":
    #     candidatos = Cands.objects.filter(corporation=corp, id_dept=dept_id ).order_by('name_can')
    # ## elif (corp=="JAL" or dept_id==10) and (corp is not None and corp !='' and dept_id!=0 and mun_id!=0 and com_id!=0):
    # el
    if (corp and dept_id and mun_id and com_id):
        candidatos = Cands.objects.filter(corporation=corp, id_dept=dept_id, id_mun=mun_id,id_com=com_id).order_by('name_can')  
    elif(corp and dept_id and mun_id):
        candidatos = Cands.objects.filter(corporation=corp, id_dept=dept_id, id_mun=mun_id).order_by('name_can')  
    
    # if (corp and dept_id and mun_id and com_id):
    #     candidatos = Cands.objects.filter(id_dept=dept_id, id_mun=mun_id,id_com=com_id).order_by('name_can')  
    # elif(corp and dept_id and mun_id):
    #     candidatos = Cands.objects.filter(id_dept=dept_id, id_mun=mun_id).order_by('name_can')  
    # print(candidatos)
    # print('candidatos',candidatos)
    # return JsonResponse(list(candidatos.values('id_ct', 'name_can')), safe=False) 
    # print('corp', corp)
    if candidatos and candidatos.exists():   
        return JsonResponse(list(candidatos.values('id_ct', 'name_can')), safe=False) 
    else:
        # return render(request,'login/index.html',{})
        return JsonResponse(list(), safe=False) 

def user_login(request):
    if request.method == 'POST':
                
        candidato =  int(request.POST.get('candidato')) if request.POST.get('candidato') else None 
        email = request.POST.get('email')
        
        print('candidato',candidato)
        print('email',email)

        #user = authenticate(request, username=username, password=password)
        
        user = Cands.objects.filter(id_ct=candidato,email=email).first()
        if user is not None:
            # if not user.is_active:                
                # hilo = threading.Thread(target=enviar_email_activacion, args=(user,))
                # hilo.start()
                # return render(request, 'login/index.html', {'info': f'Se ha enviado un correo de activación. Revisa tu correo {user.email}. Debes activar tu cuenta e iniciar sesión nuevamente.'})
            # elif user.must_change_password:
            #     return redirect('asamblea:password_change_first_login')
            # else:
            
            login(request, usuario_sistema.objects.get(username=user.email))
            return JsonResponse({"status" : "ok", "action" : "testigos"}, status=200 ) 
            #return redirect('testigos:home')
        else:
            return JsonResponse({"status" : "error", "action" : f'El candidato que seleccionó no está registrado en la plataforma del partido verde con <a href="https://sirav.alianzaverde.org.co/cuenta/login/">{ email }</a>.<br><br><b>Por favor, <a href="https://sirav.alianzaverde.org.co/cuenta/login/">HAGA CLIC AQUÍ</a> para verificar que correo tiene asociado</b>'} ) 

           # return render(request, 'login/index.html', {"status" : "error", 'action': f"El candidato que selecciono no está registrado en la plataforma del partido verde con {{correo}}. <b>Por favor, <a href='https://sirav.alianzaverde.org.co/cuenta/login/'>HAGA CLIC AQUÍ</a> para verificar que correo tiene asociado</b>"})

            # return render(request, 'login/index.html', JsonResponse({"status" : "error", "action" : "El candidato que selecciono no está registrado en la plataforma del partido verde con correo. <b>Por favor, <a href='https://sirav.alianzaverde.org.co/cuenta/login/'>HAGA CLIC AQUÍ</a> para verificar que correo tiene asociado</b>"}, status=400 ))
    ##return render(request, 'login/index.html')
    

class Testigos( generic.TemplateView):
    template_name = 'index.html'
    #login_url='testigos:home'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)                
        candidato:Cands = getCandidato(self.request)
        context["candidato"] = candidato
        context["departamento"] = candidato.id_dept.name_dept if candidato.id_dept else ''
        context["municipio"] = candidato.id_mun.name_mun if candidato.id_mun else ''
        context["comunidad"] = candidato.id_com.name_com if candidato.id_com else ''
        
        try:
            divi_dept=int(candidato.id_dept.cod_dep)
        except:
            divi_dept= None
        try:
            divi_mun=int(candidato.id_mun.cod_mun)
        except:
            divi_mun= None  
        
        try:
            divi_coms=int(candidato.id_com_id)
        except:
            divi_coms= None  
        
        zonas = None
        puestos = None
        mesas = None
        if (divi_dept  and divi_mun ):             
            #.exclude(comuna_localidad__isnull=True)\
            #.exclude(comuna_localidad__exact='')\
            zonas= Divipole.objects.filter(dd=divi_dept,mm=divi_mun) \
            .values('zz','zz') \
            .annotate(total_votantes=Count('total')) \
            .order_by('zz')

        print('dept',divi_dept)
        print('municipio',divi_mun)
        print('comuna',divi_coms)
        print('zonassssss',zonas)
        #print(zonas.count())
        context["zonas"] = zonas
                
        if (divi_dept and divi_mun ):   
            puestos= Divipole.objects.filter(dd=divi_dept,mm=divi_mun) \
            .values('id','nombre_puesto') \
            .annotate(total_votantes=Count('total')) \
            .order_by('id')
        context["puestos"] = puestos    
        
        if (divi_dept and divi_mun and divi_coms ):   
            mesas= Divipole.objects.filter(dd=divi_dept,mm=divi_mun,pp= divi_coms )\
                .values('id', 'mesas','mesas_ocupadas')\
                    .order_by('nombre_puesto')
            #.values('id','nombre_puesto') \
            # .annotate(total_votantes=Count('total')) \
            # .order_by('id')    
            
    
        print('mesas * ', mesas)
        num=0
        mesas_ocupadas= []
        if mesas:
            num =mesas[0]['mesas']
            mesas_ocupadas = list(mesas[0]['mesas_ocupadas']) if mesas[0]['mesas_ocupadas'] else []
        if num >0:    
            # mi_lista = [i for i in range(1, num)]    
            mi_lista = []
            for i in range(num):
                if (i+1) not in mesas_ocupadas:                
                    mi_lista.append({'id':int(i+1) , 'nombre_mesa':'Mesa '+str(i+1)})
        #     return JsonResponse((mi_lista), safe=False) 
        # else:
        #     return JsonResponse(list(), safe=False)    
            
            
    
        #context["mesas"] = mi_lista    
        
        
            
        return context


def data(request):
    # if request.method == 'POST':
    # else
    # try:
    #     candidato = Cands.objects.filter(email=request.user.email).first()
    # except Cands.DoesNotExist:
    #     candidato = None
    # print(candidato)
    type = request.GET.get('type_testigos')
    print(request.user.id)
    print('type',type)
    lista_ = Zonas.objects.filter(id_user=request.user.id, type_witnesse=type)
    
    return JsonResponse(list(lista_.values('id_t','id_z_mun__name_mun',
                                           #'name_post', ''
                                            'name_table'
                                           , 'cc'
                                           , 'p_name'
                                           , 's_name'
                                           , 'p_last_name'
                                           , 's_last_name'
                                           , 'email'
                                           , 'phone')), safe=False) 


def guardar_testico_mesa(request):
    if request.method == 'POST':
        
        id = request.POST.get('id')
        cc= request.POST.get('cc')
        type_witnesse=request.POST.get('type')
        p_name=request.POST.get('p_name')
        s_name=request.POST.get('s_name')
        p_lastname=request.POST.get('p_lastname')
        s_lastname=request.POST.get('s_lastname')
        phone=request.POST.get('phone')
        email=request.POST.get('email')        
        save=request.POST.get('save')
        mesas=request.POST.get('mesas')
        zona=request.POST.get('zona')
        puesto=request.POST.get('puesto')
        
        data = {}
        error =""

        if (save=='1'):
            if (mesas==""):
                error = "Debe seleccionar al menos una mesa"
                #data = []
            elif (cc=="" or p_name=="" or p_lastname=="" or phone=="" or email==""):
                error = "No se puede registrar este usuario, ya que los datos requeridos deben estar diligenciados"
                #data = []
            else:
                if (type_witnesse =="escrutinio"):
                    pass
                    #rep = new ConfigureSentence("t_zonas");
                else:                
                    # name_table 
                    # type_witnesse 
                    # cc 
                    # p_name 
                    # s_name 
                    # p_last_name 
                    # s_last_name 
                    # email 
                    # phone 
                    # id_z_mun 
                    # id_z_dept 
                    # save_testigos 
                    # id_user 
                    # date_creacion 
                    # date_export 
                    # status_export 
                    # status_error 
                    # desc_error 
                    candidato:Cands = getCandidato(request)
                    
                    t_zonas =Zonas.objects.create(
                        name_table= id,
                        type_witnesse= type_witnesse,
                        cc= cc,
                        p_name=p_name, 
                        s_name= s_name,
                        p_last_name=p_lastname, 
                        s_last_name= s_lastname,
                        email= email,
                        phone= phone,
                        id_z_mun= candidato.id_mun, 
                        id_z_dept= candidato.id_dept,
                        save_testigos=save, 
                        id_user= request.user.id,
                        # date_creacion=, 
                        # date_export= ,
                        status_export= 0, 
                        status_error = 0,
                        # desc_error =
                    )
     
                    lista = list(map(int, mesas.split(',')))  # [1, 2, 3]
                    divi = Divipole.objects.get(id=puesto)                    
                    for l in lista:                        
                        if not hasattr(divi, 'mesas_ocupadas') or divi.mesas_ocupadas is None:
                            divi.mesas_ocupadas = []
                        if l not in divi.mesas_ocupadas:
                            divi.mesas_ocupadas.append(l)                    
                    divi.save()
                    error="ok"
                    return JsonResponse({"status" : "ok", "action" : "/testigos"}, status=200 )
                    # return redirect('/testigos')
                    
                    # div= Divipole.objects.filter(id=puesto).update(mesas_ocupadas=[lista])
                    #rep = new ConfigureSentence("t_tables");
                
                #data = $rep->update($data, "id_t=" . $id);
            
        #else:
            #if ($type=="escrutinio"):
                #$rep = new ConfigureSentence("t_zonas");
            #} else {
                #$rep = new ConfigureSentence("t_tables");
            #}
            #$data = $rep->update($data, "id_t=" . $id);
            
        
        return JsonResponse({'data': data,'error': error})
    #return 
    #return render(request, 'index.html', {})