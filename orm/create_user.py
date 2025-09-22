from django.contrib.auth.models import User
from testigos.models import *
can= Cands.objects.all().filter(email__in=[
'efrainsanchez.0126@gmail.com',
'estupinandanna18@gmail.com',
'rubbyrodriguez382@gmail.com',
'lisbethgutierrez072@gmail.com',
'jaiderdanielvargastorres876@gmail.com',
'alanlallemand0320@gmail.com'
    
])
for c in can:
    if not User.objects.filter(username=c.email).exists():
        try:
            print(f'Creando usuario para {c.name_can} - {c.email}')
            usuario = User.objects.create_user(username=c.email, email=c.email, password="Colombia2025*", first_name=c.name_can)
        except:
            print(f'Error creando usuario para {c.name_can} - {c.email}')   
            

