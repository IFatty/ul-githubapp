# BUSCADOR USUARIOS GITHUB #
---
Esta aplicación permite realizar la búsqueda de usuarios de GitHub utilizando su [API pública](https://api.github.com/users)

### REQUERIMIENTOS GENERALES DEL TRABAJO ###
---
* Crear un nuevo directorio en su repositorio con su nombre de proyecto API.
* Publicar sus ejemplos en el repositorio.
* Editar un archivo README.md.
* Asignar nombre al proyecto API.
* Adicionar nombre(s) del(los) estudiante(s) (y código(s)).
* Sitio web y descripción del proyecto API.
* Adicionar pasos para obtener registros (con la creación de claves si es necesario).
* Referenciar bibliotecas utilizadas y pasos para instalarlas.
* Adicionar pasos para usar y probar los ejemplos que construye.
* Cargar solución a Github -> 15%.
* Presentar su proyecto API en clase (sábado, 17 de junio) -> 5%.

### DEPENDENCIAS ###
---
+ [Python](https://www.python.org/downloads/)
+ [Django](https://www.djangoproject.com/)

### LIBRERÍAS ###
---
+ Requests

### GESTIÓN DE DEPENDENCIAS ###
---
Para la gestión de dependencias se recomienda utilizar el gestor `pip` de la siguiente manera:
```
pip install django
pip install requests
```

### EJECUCIÓN DE LA APLICACIÓN ###
---
Para acceder a la aplicación es necesario realizar la ejecución del servidor local, para lo cual se debe ejecutar en la carpeta `raíz->src` de la solución el comando:
```
py manage.py runserver
```
Una vez realizada su ejecución, se levantará una instancia del servidor en el equipo local sobre el puerto 8000 que es el puerto por defecto, posteriormente se deberá abrir el navegador web de preferencia e ir a la dirección [localhost:8000/githubapp/](http://localhost:8080/githubapp).