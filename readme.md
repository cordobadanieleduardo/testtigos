

mkdir testigos

py -m venv ..\venv
..\venv\Scripts\activate.bat

pip install django
pip install mysqlclient
pip install psycopg[binary]

django-admin startproject app testigos

cd testigos

 py manage.py createsuperuser



  python manage.py runserver