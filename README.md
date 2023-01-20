# Prueba Técnica
## Joel Guerrero



La prueba técnica se encuentra escrita en Python, en Django. Las librerías utilizadas son las siguientes:

- Django
- djangorestframework
-
## Features

- Api Rest para el Endpoint de creación de Citación (Multa)
- Portal Básico para el CRUD de officer
- Visualización de citaciones
- Portal Admin


## Installation

Seguir los pasos a continuación

```sh
python -m venv venv
.\venv\Scripts\activate
python -m pip install -r requirements.txt
```

Para correr las migraciones y aplicar los permisos...

```sh
python manage.py migrate
python ./utils.py
```

## Explicación

El proyecto utiliza una base de datos sqlite3, al crear las migraciones se crea un usuario superusuario con las siguientes credenciales

#### user: admin 
#### password: P@ssw0rd

Para correr el servidor se ejecuta:

```sh
python manage.py runserver
```
Con el usuario anterior se puede acceder al Porta administrador de Django, en la siguiente ruta: `http://localhost:8000/admin`

El usuario **Clerk** no tiene formulario en el portal, por lo que es necesario crearlo desde el Admin, para esto seguimos los siguientes pasos:

- Creamos un usuario
- Editamos ese usuario y activamos para que este sea un staff
- Creamos un Clerk con el usuario antes agregado.

## EndPoint
El Endpoint para la creacion de citación es el siguiente:
`http://127.0.0.1:8000/api/citation/`

A través del protocolo **Http** y con el método **POST**, la autenticación es Básica, por lo que se debe utilizar **Basic AUTH**, las credenciales del Oficial.

Las rutas del Portal son las siguientes:

- '/api/ '=> Acceso a la API
- '/' => home
- '/login/' => login
- '/logout/' => logout
- '/officer/' => list-officer
- '/officer/create/'=> 'create-officer'
- '/officer/update/<int:id>'=>'update-officer'
- '/officer/detail'=>'detail-officer'
- '/officer/delete/<int:id>'=> 'delete-officer'
- '/citation/'=> 'list-citation'
- '/citation/detail/<int:id>' => 'detail-citation'