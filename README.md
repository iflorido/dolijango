# dolijango
Migración de las funcionalidades de Dolibarr a Django Python  
Proyecto Personal para adquirir experiencia en Django.

# Paso 1
Instalación de la libreria pip install Django
# Paso 2 Creamos el proyecto llamado doli_jango
django-admin startproject doli_jango
# Paso 3 Una vez creado el proyecto vamos a crear la aplicación que la llamaremos DoliJangoApp
django-admin startapp DoliJangoApp
# Paso 4, Probamos nuestra aplicación con 
python manage.py runserver
# Paso 4.1 Nos mostrara un mensaje para aplicar migraciones no realizadas, lo hacemos con el comando 
python manage.py migrate
# Paso 5 Instalamos La API Rest que usaremos.
pip install djangorestframework
# Paso 6 añadimos el archivo de dependencias, así al querer ejecutar el proyecto en otra maquina no tendremos problemas.
pip freeze > requirements.txt

# Paso 6 Crear el super usuario para la administración
python manage.py createsuperuer 
Nos pedirá el usuario, en este caso iflorido, nuestro correo y una contraseña