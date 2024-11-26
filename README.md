# Proyecto Django con Bootstrap 5

Este proyecto proporciona una guía paso a paso para crear una aplicación Django utilizando **Bootstrap 5** para el diseño de interfaces.

---

## Tabla de Contenidos
- [Requisitos](#requisitos)
- [Configuración del Entorno](#configuración-del-entorno)
- [Activación del Entorno](#Activación-del-Entorno)
- [Instalar Django y Guardar dependencias](Instalar-Django-y-Guardar-dependencias)
- [Pasos del Proyecto](#pasos-del-proyecto)
  - [Configuración Inicial](#configuración-inicial)
  - [Configuración del Proyecto](#configuración-del-proyecto)
  - [Creación de Vistas y Modelos](#creación-de-vistas-y-modelos)
  - [Integración de Bootstrap 5 por CDN](#integración-de-bootstrap-5-por-CDN)
  - [Creación del SuperUsuario Y Configuraciones](#Creación-del-SuperUsuario-Y-Configuraciones)


---

## Requisitos

- Python 3.9 o superior
- Django 4.0 o superior
- Bootstrap 5

---

## Configuración del Entorno

1. Crear el entorno virtual:
   ```bash
   python -m venv venv


## Activación del Entorno

2. Activar el entorno virtual:
    ### Windows
    ```bash
    venv\Scripts\activate

## Configuración Inicial
## Instalar Django y Guardar dependencias

3. Intalación Django
    ```bash
    pip install django

4. Instalamos la actualizacion de pip
    ```bash
    python.exe -m pip install --upgrade pip

## Guardar las dependencias
5. Instalación dependencias
    ```bash
   pip freeze > requirements.txt

## Pasos del Proyecto
6. Crear el Proyecto
    ```bash
    django-admin startproject lunes

6. Ingresar al directorio del Proyecto
    ```bash
    cd lunes

7. Creamos la Aplicación applunes
    ```bash
    python manage.py startapp applunes

## Configuración del Proyecto

8. Conectar el proyecto con la aplicación: Agregar 'applunes' en la lista INSTALLED_APPS dentro del archivo lunes/settings.py:
    ```bash
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'applunes',
    ]
## Creación de vistas y modelos
11. Creo el urls.py en applunes 

12. Leccion3/urls, le damos la ruta para que conozca app1.urls

    ```bash
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('',include('applunes.urls')),
    
    ]
13. No vamos a applunes/views.py
    
    ```bash
    from django.views.generic import ListView
    from .models import Item

    class ItemListView(ListView):
        model = Item
        template_name = 'item_list.html'
        context_object_name = 'items'
        paginate_by = 10

14. applunes/models.py

     ```bash
    from django.db import models
    from django.core.exceptions import ValidationError

    class Item(models.Model):
        name = models.CharField(max_length=100)
        description = models.TextField()
        price = models.DecimalField(max_digits=10, decimal_places=2)
        created_at = models.DateTimeField(auto_now_add=True)

        class Meta:
            ordering = ['-created_at']  # Orden por fecha descendente

        def clean(self):
            if self.price <= 0:
                raise ValidationError('El precio debe ser mayor que cero.')

        def __str__(self):
            return self.name

15. en applunes creamos una Carpeta llamada templates creamos un archivo llamado index.html app1\templates\item_list.html

     ```bash
   <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>

    <body>
        <h1>Items</h1>
        {% if items %}
        <ul role="list">
            {% for item in items %}
            <li role="listitem">
                <strong>{{ item.name }}</strong> - ${{ item.price }}
                <p>{{ item.description }}</p>
            </li>
            {% endfor %}
        </ul>

        <!-- Navegación de Paginación -->
        <div>
            <span>
                {% if items.has_previous %}
                <a href="?page=1">Primera</a>
                <a href="?page={{ items.previous_page_number }}">Anterior</a>
                {% endif %}

                <span class="current">
                    Página {{ items.number }} de {{ items.paginator.num_pages }}
                </span>

                {% if items.has_next %}
                <a href="?page={{ items.next_page_number }}">Siguiente</a>
                <a href="?page={{ items.paginator.num_pages }}">Última</a>
                {% endif %}
            </span>
        </div>
        {% else %}
        <p>No hay elementos disponibles.</p>
        {% endif %}

        <div>
            <h2>Example Image</h2>
        </div>
</body>

</html>

12. Crear el archivo urls.py en applunes -> applunes/urls.py

    ```bash
    from django.urls import path
    from applunes.views import ItemListView

    urlpatterns = [
        path('', ItemListView.as_view(), name='item')
    ]

14. colocamos los siguientes comandos
    
    ```bash
    python manage.py makemigrations
    python manage.py migrate

15. Hacemos Correr en el Servidor nuestra Aplicación

    ```bash
    python manage.py runserver

16. Comprobamos en las paginas las rutas http://127.0.0.1:8000/app1/

17. Generamos la carpeta templates en la app2 y creamos el archivo productos.html
    ```bash
    <!DOCTYPE html>
    <html>

    <head>
        <title>Lista de Productos</title>
    </head>

    <body>
        <h1>Productos Disponibles</h1>
        <ul>
            {% for producto in productos %}
            <li>
                <strong>{{ producto.nombre }}</strong> - ${{ producto.precio }}<br>
                {{ producto.descripcion }}
            </li>
            {% endfor %}
        </ul>
    </body>

    </html>
18. en la leccion3/urls.py incluimos el path('app2/', include('app2.urls))
    
    ```bash
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('app1/',include('app1.urls')),
        path('app2/',include('app2.urls')),
    ]
19. en app2 creo un archivo urls.py
    ```bash
    from django.urls import path
    from app2 import views


    urlpatterns = [
        path('',views.productos, name='producto'),
    ]

20. Creamos el modelo en app2/models.py

    ```bash
    from django.db import models

    class Producto(models.Model):
        nombre = models.CharField(max_length=100)
        precio = models.DecimalField(max_digits=10, decimal_places=2)
        descripcion = models.TextField()

        def __str__(self):
            return self.nombre

21. Configuramos la vista y agregamos el modelo en app2/views.py

    ```bash
    from django.shortcuts import render
    from .models import Producto

    def productos(request):
        productos = Producto.objects.all()
        return render(request, 'productos.html', {'productos': productos})

22. Escribimos comandos de migracion a la base de datos

    ```bash
    python manage.py makemigrations
    python manage.py migrate

23. Ingresando el comando en la shell con el objetivo de Cargar datos en la base de datos con los siguientes códigos
    ```bash
    python manage.py shell

24. Vamos a Cargar datos en la Bases de Datos
    ```bash
    from app2.models import Producto

    Producto.objects.create(nombre="Laptop", precio=1200.00, descripcion="Laptop de alta gama")
    Producto.objects.create(nombre="Mouse", precio=25.99, descripcion="Mouse inalámbrico")
    Producto.objects.create(nombre="Teclado", precio=45.00, descripcion="Teclado mecánico")

25. Verificar que los datos se insertaron correctamente
    ```bash
    productos = Producto.objects.all()
    for producto in productos:
        print(producto.nombre, producto.precio, producto.descripcion)

    # para salir de la shell
    exit()

26. Nos fijamos en db.sqlite3 para ver si los datos estan en la base de datos

27. Corremos el servidor 
    ```bash
    python manage.py runserver

28. Verificamos la nueva aplicación app2, que debe contener los modelos y Bd
    ```bash
    127.0.1:8000/app2/

29. En leccion3 vamos a crear la carpeta templates en la principal leccion3/templates, y si es por consola 
    ```bash
    mkdir templates

30. Dentro de la Carpeta que creamos templates vamos agregar include leccion3/templates/include y si es por consola
    ```bash
    cd templates
    mkdir include

31. Creamos base.html En la carpeta templates/include/base.html
    ```bash
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <title>{% block title %}{% endblock %}</title>
    </head>

    <body>
        {% block content %}
        {% endblock %}
    </body>

    </html>

32. Cambiamos en app1/templates/index.html y colocamos esto:
    ```bash
    {% extends 'base.html' %}

    {% block title%}index{% endblock%}

    {% block content %}
    <h1>Pagina Inicial</h1>
    {% endblock%}

33. Cambiamos también app2/templates/producto.html y colocamos esto:
    ```bash
    {% extends 'base.html' %}

    {% block title%}Productos{% enblock%}

    {% block content %}
    <h1>Productos Disponibles</h1>
    <ul>
        {% for producto in productos %}
        <li>
            <strong>{{ producto.nombre }}</strong> - ${{ producto.precio }}<br>
            {{ producto.descripcion }}
        </li>
        {% endfor %}
    </ul>
    {% endblock%}

34. Vamos a leccion3/setting.py en el proyecto y agregamos  'DIRS': [BASE_DIR, 'templates'],
    ```bash
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR, 'templates'],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
35. Si no esta corriendo el Servidor activelo
    ```bash
    python manage.py runserver

36. Verificamos las paginas 
    ```bash
    http://127.0.0.1:8000/app1/
    http://127.0.0.1:8000/app2/

## Integración de Bootstrap 5 por CDN

37. Vamos a cambiar el templates/include/base.html y agregamos el cdn de Bootsrap5.3 e incluimos header y footer
    ```bash
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{% block title %}{% endblock %}</title>
        <!-- Bootstrap CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="bg-light text-dark">
        
        <!-- include Header.html -->
        {% include 'include/header.html' %}

        {% block content %}
            <!--dentro del block content se mostrará contenido dinamico -->
            <!--mostrare index.html - productos.html - vista1.html - vista2.html -->
            <!--mostrare cada html cuando el usuario lo pida -->
        {% endblock %}

        <!-- include Footer.html -->
        {% include 'include/footer.html' %}

        <!-- Bootstrap JS (opcional) -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>

38. Agregamos un header en el templates/include/header.html
    ```bash
    <div class="container mt-5">
        <header class="text-center mb-4">
            <h1 class="display-4">Falabella</h1>
            <p class="lead">Email: <a href="mailto:falabella@example.com"
                    class="text-decoration-none">falabella@example.com</a></p>
            <p class="lead">Teléfono: <a href="tel:+56123456789" class="text-decoration-none">+56 123 456 789</a></p>
            <a href="/app1/">Inicio</a>
            <a href="/app2/">Productos</a>
        </header>
    </div>

39. Agregamos un footer en el templates/include/footer.html
    ```bash
    <footer>este es un footer</footer>

40. Creamos Otra aplicacion la app3
    ```bash
    python manage.py startapp app3 
    
41. En Leccion3/setting.py agregamos la aplicación app3  
    ```bash
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'app1',
        'app2',
        'app3',
    ]
42. al crear app3 tenemos que ingresar la ruta en el proyecto leccion3/urls. y agregamos path('app3/',include('app3.urls')),
    ```bash
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('app1/',include('app1.urls')),
        path('app2/',include('app2.urls')),
        path('app3/',include('app3.urls')),
    ]
43. Agregamos en la app3 agregamos templates/vista1.html 
    ```bash
    {% extends 'base.html' %}

    {% block title %}Vista 1 App3{% endblock %}

    {% block content %}
    <h1>Soy la vista 1 de la App3</h1>
    {% endblock %}

44. Agregamos en la app3 agregamos templates/vista2.html
     ```bash
    {% extends 'base.html' %}

    {% block title %}Vista 2 App3{% endblock %}

    {% block content %}
    <h1>Soy la vista 2 de la App3</h1>
    {% endblock %}
45. Vamos a cambiar los templates de todas las aplicaciones agregando el nombre de la aplicación ejemplos para hacer
    ```bash
    templates\app1\index.html
    templates\app2\productos.html
    templates\app3\vista1.html
    templates\app3\vista2.html

46. Configure la views.py en app3 -> renderize las paginas que se hizo en la vista1.html y vista2.html
    ```bash
    from django.shortcuts import render

    def vista1(request):
        return render(request, 'vista1.html')

    def vista2(request):
        return render(request, 'vista2.html')

47. Crea en app3/urls.py y configura la urls.
      ```bash
    from django.urls import path
    from app3 import views

    urlpatterns = [
        path('vista1/',views.vista1, name='vista1'),
        path('vista2/',views.vista2, name='vista2'),
    ]

48. Si no esta corriendo el Servidor activelo
    ```bash
    python manage.py runserver

49. Hay que cambiar en las vistas de todas las aplicaciones app1, app2 y app3 la carpetas de las views EN app1/views.py
    ```bash
    from django.shortcuts import render

    # Create your views here.
    def index(request):
        return render(request, 'app1/index.html')

50. Hay que cambiar en las vistas de todas las aplicaciones app1, app2 y app3 la carpetas de las views EN app2/views.py 
    ```bash
    from django.shortcuts import render
    from .models import Producto

    def productos(request):
        productos = Producto.objects.all()
        return render(request, 'app2/productos.html', {'productos': productos})


51. Hay que cambiar en las vistas de todas las aplicaciones app1, app2 y app3 la carpetas de las views EN app3/views.py 
    ```bash
    from django.shortcuts import render

    def vistas1(request):
        return render(request, 'app3/vista1.html')

    def vistas2(request):
        return render(request, 'app3/vista2.html')

52. Actualizamos el header.html que se encuentra en templates/include/header.html y se agrega app3/vista1 y app3/vista2
    ```bash
    <div class="container mt-5">
        <header class="text-center mb-4">
            <h1 class="display-4">Falabella</h1>
            <p class="lead">Email: <a href="mailto:falabella@example.com"
                    class="text-decoration-none">falabella@example.com</a></p>
            <p class="lead">Teléfono: <a href="tel:+56123456789" class="text-decoration-none">+56 123 456 789</a></p>
            <a href="/app1/">Inicio</a>
            <a href="/app2/">Productos</a>
            <a href="/app3/vista1/">Vista1</a>
            <a href="/app3/vista2/">Vista2</a>
        </header>
    </div>   
53. Colocar la ruta vista1 y vista2 en app3/urls.py
     ```bash
    from django.urls import path
    from app3 import views

    urlpatterns = [
        path('vista1/',views.vista1, name='vista1'),
        path('vista2/',views.vista2, name='vista2'),
    ]
54. Volvemos Activar el Servidor para Ver los Cambios 
    ```bash
    python manage.py runserver

## Creación del SuperUsuario Y Configuraciones
55. Creamos un superusuario 
    ```bash
    python manage.py createsuperuser

56. Verificamos usuario y contraseña del superuser por motivos de aprendizaje le vamos a dar estos parametros pero que no son seguros
    ```bash
    admin
    admin@gmail.com
    admin1234
    y

57. Volvemos Activar el Servidor para Ver los Cambios 
    ```bash
    python manage.py runserver

58. Para que el administrador pueda ver las tablas y los registro en la base de datos app2, tiene que ir app2/admin.py

    ```bash
    from django.contrib import admin
    from .models import Producto
    # Register your models here.

    admin.site.register(Producto)



