# Proyecto Django de Vista por Clases

Este proyecto proporciona una guía paso a paso para crear una aplicación Django utilizando **De Vista por Clases** para el diseño de interfaces.

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



