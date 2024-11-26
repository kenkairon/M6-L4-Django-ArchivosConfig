# Proyecto Django de Vista por Clases y Funciones

Este proyecto proporciona una guía paso a paso para crear una aplicación Django utilizando **De Vista por Clases y Funciones** para el diseño de interfaces.

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

16. Crear el archivo urls.py en applunes -> applunes/urls.py

    ```bash
    from django.urls import path
    from applunes.views import ItemListView

    urlpatterns = [
        path('', ItemListView.as_view(), name='item')
    ]

17. colocamos los siguientes comandos
    
    ```bash
    python manage.py makemigrations
    python manage.py migrate

18. Hacemos Correr en el Servidor nuestra Aplicación

    ```bash
    python manage.py runserver

19. Cargamos datos en la base de datos con el archivo dataShell.txt

20. Aplicamos el comando en la 

    ```bash
    python manage.py shell

21. En la consola vamos a pegar esta información para que nos carge información en la base de datos

    ```bash
    from applunes.models import Item

    # Datos de ejemplo
    from applunes.models import Item

    # Datos de ejemplo
    items_data = [
        {"name": "Smartphone", "description": "Teléfono inteligente con pantalla AMOLED y 128GB de almacenamiento.", "price": 799.99},
        {"name": "Tablet", "description": "Tablet de 10 pulgadas ideal para leer y trabajar en movimiento.", "price": 399.99},
        {"name": "Smartwatch", "description": "Reloj inteligente con GPS y monitoreo de salud.", "price": 199.99},
        {"name": "Auriculares Bluetooth", "description": "Auriculares inalámbricos con batería de larga duración.", "price": 49.99},
        {"name": "Cámara DSLR", "description": "Cámara digital de alta calidad con lentes intercambiables.", "price": 1200.00},
        {"name": "Disco Duro Externo", "description": "Almacenamiento portátil de 1TB con USB 3.0.", "price": 59.99},
        {"name": "Impresora", "description": "Impresora multifuncional con conexión WiFi.", "price": 89.99},
        {"name": "Silla Gamer", "description": "Silla ergonómica diseñada para largas sesiones de juego.", "price": 159.99},
        {"name": "Teclado Mecánico", "description": "Teclado mecánico con retroiluminación personalizable.", "price": 109.99},
        {"name": "Monitor Curvo", "description": "Monitor curvo Full HD de 24 pulgadas.", "price": 249.99},
        {"name": "Router WiFi", "description": "Router de alta velocidad con doble banda.", "price": 69.99},
        {"name": "Proyector", "description": "Proyector portátil para presentaciones y entretenimiento.", "price": 349.99},
        {"name": "Micrófono USB", "description": "Micrófono profesional para grabación y streaming.", "price": 89.99},
        {"name": "Altavoz Bluetooth", "description": "Altavoz portátil resistente al agua.", "price": 39.99},
        {"name": "Webcam HD", "description": "Cámara web con resolución HD 1080p y micrófono integrado.", "price": 49.99},
    ]

    # Carga de datos en la base de datos
    for item_data in items_data:
        item, created = Item.objects.get_or_create(**item_data)
        if created:
            print(f"Item creado: {item.name}")
        else:
            print(f"Item ya existente: {item.name}")

    # enter
    exit()

22. Creo Una rama vista por clase para respaldar la información contenida en los procesos de como se hizo
    ```bash
    git branch -m vistaporclases
    git add .
    git commit -m "Agregamos vistas por clases"
    git push origin vistaporclases

23. Cambiamos la applunes\views , Con el Objetivo de Trabajar con funciones en este proyecto
      ```bash
    from typing import Any
    from django.http import HttpRequest, HttpResponse
    from django.shortcuts import render
    from django.core.paginator import Paginator
    from django.db import DatabaseError
    from .models import Item

    # Create your views here.

    def item_list(request: HttpRequest) -> HttpResponse:
        try:
            items = Item.objects.all()
        except DatabaseError:
            items = []

        paginator = Paginator(items, 10)  # 10 ítems por página
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'applunes/item_list.html', {'items': page_obj})

24. Cambiamos el templates\applunes\item_list.html
25. en carpeta lunes(principal) creamos un templates\base.html
    ```bash
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        {% block content %}
        {% endblock%}

    </body>
    </html>
26. Cambiamos la vista por clase por la lista por funciones applunes\views.py
    ```bash
    from django.urls import path
    from . import views

    app_name = 'applunes'

    urlpatterns = [
        path('', views.item_list, name='item_list'),
    ]

27. Cambiamos el templates\applunes\item_list.html
    ```bash
    {% extends 'base.html' %}
    <!--{% load static %}-->

    {% block title %}Item List{% endblock %}

    {% block content %}
        <h1>Items</h1>
        <button id="theme-toggle">Toggle Theme</button>

        {% if items %}
            <ul class="item-list" role="list">
                {% for item in items %}
                    <li role="listitem">
                        <strong>{{ item.name }}</strong> - ${{ item.price }}
                        <p>{{ item.description }}</p>
                    </li>
                {% endfor %}
            </ul>

            <!-- Navegación de Paginación -->
            <div class="pagination">
                <span class="step-links">
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
            <img src="{% static 'images/django.png' %}" alt="Logotipo de Django" style="width: 200px; height: auto;">
        </div>
    {% endblock %}

28. Vamos al archivo de configuración lunes\settings.py , Agregamos  'DIRS': [BASE_DIR,'templates'], para que nos lea los templates
     ```bash
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR,'templates'],
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

29. Agregamos los cambios a una rama llamada extends
    ```bash
    git add .
    git commit -m "extendiendo a base.html"
    git branch -m extends
    git push origin extends

30. Cambiamos el templates/base.html
    ```bash
    <!DOCTYPE html>
    <html lang="es">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="Una aplicación de Django con estructura base.">
        <link rel="icon" href="{% static 'images/favicon.ico' %}">
        <title>{% block title %}My Project{% endblock %}</title>

        
        <!-- Estilos principales -->
        <!--<link rel="stylesheet" href="{% static 'css/header.css' %}">-->
        <!-- <link rel="stylesheet" href="{% static 'css/footer.css' %}"-->
        <!--<link rel="stylesheet" href="{% static 'css/item_list.css' %}"> -->
        <link rel="stylesheet" href="{% static 'css/styles.css' %}">

        <!-- JavaScript principal -->
        <script src="{% static 'js/main.js' %}" defer></script>
    </head>

    <body class="light-mode">

        <main>
            {% block content %}{% endblock %}
        </main>

    </body>

    </html>

31. en la carpeta principal lunes agregamos static lunes/static
32. en el static vamos a crear la carpeta images, css y js
33. en static/css/styles.css creamos el css correspondiente
    ```bash
    /* static/css/style.css */
    body.light-mode {
        background-color: #f4f4f9;
        color: #333;
    }

    body.dark-mode {
        background-color: #333;
        color: #f4f4f9;
    }

    button {
        margin: 10px;
        padding: 10px;
        background-color: #007bff;
        color: #fff;
        border: none;
        border-radius: 5px;
    }

34. en static/js/main.css creamos el js correspondiente
    ```bash
    // static/js/main.js
    document.addEventListener("DOMContentLoaded", function () {
        const toggleButton = document.getElementById("theme-toggle");
        const body = document.body;

        // Cargar tema guardado en localStorage
        const savedTheme = localStorage.getItem("theme");
        if (savedTheme) {
            body.className = savedTheme;
        }

        toggleButton.addEventListener("click", function () {
            // Alternar entre los modos claro y oscuro
            if (body.classList.contains("dark-mode")) {
                body.classList.remove("dark-mode");
                body.classList.add("light-mode");
                localStorage.setItem("theme", "light-mode");
            } else {
                body.classList.remove("light-mode");
                body.classList.add("dark-mode");
                localStorage.setItem("theme", "dark-mode");
            }
        });
    });

35. en el static/images vamos agregar la images/django.png

36. en el archivo templates/applunes/item_list.html le sacamos el comentario  <!--{% load static %}-->

    ```bash
    {% extends 'base.html' %}
    {% load static %}

    {% block title %}Item List{% endblock %}

    {% block content %}
        <h1>Items</h1>
        <button id="theme-toggle">Toggle Theme</button>

        {% if items %}
            <ul class="item-list" role="list">
                {% for item in items %}
                    <li role="listitem">
                        <strong>{{ item.name }}</strong> - ${{ item.price }}
                        <p>{{ item.description }}</p>
                    </li>
                {% endfor %}
            </ul>

            <!-- Navegación de Paginación -->
            <div class="pagination">
                <span class="step-links">
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
            <img src="{% static 'images/django.png' %}" alt="Logotipo de Django" style="width: 200px; height: auto;">
        </div>
    {% endblock %}

37. En el templates/base.html comentamos <!--<link rel="icon" href="{% static 'images/favicon.ico' %}">--> y colocamos {% load static %}
    ```bash
    {% load static %}
    <!DOCTYPE html>
    <html lang="es">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="Una aplicación de Django con estructura base.">
        <!--<link rel="icon" href="{% static 'images/favicon.ico' %}">-->
        <title>{% block title %}My Project{% endblock %}</title>

        <!-- Estilos principales -->
        <!--<link rel="stylesheet" href="{% static 'css/header.css' %}">-->
        <!-- <link rel="stylesheet" href="{% static 'css/footer.css' %}"-->
        <!--<link rel="stylesheet" href="{% static 'css/item_list.css' %}"> -->
        <link rel="stylesheet" href="{% static 'css/styles.css' %}">

        <!-- JavaScript principal -->
        <script src="{% static 'js/main.js' %}" defer></script>
    </head>

    <body class="light-mode">

        <main>
            {% block content %}{% endblock %}
        </main>

    </body>

    </html>

38. Reiniciamos el Servidor para Ver los cambios

    ```bash
    python manage.py runserver

39. No me esta encontrando los archivos imagen,css,js en lunes/setting.js vamos agregar esto
```bash
    # Internationalization
    # https://docs.djangoproject.com/en/5.1/topics/i18n/

    LANGUAGE_CODE = 'es-es'
    TIME_ZONE = 'America/Santiago'

    USE_I18N = True
    USE_TZ = True



    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/5.1/howto/static-files/

    STATIC_URL = 'static/'

    STATICFILES_DIRS = [
        BASE_DIR / 'static',
    ]
