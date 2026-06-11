# 🏆 MNGTournament API - Django REST Framework

API REST desarrollada con Django REST Framework para la gestión de torneos deportivos. Este proyecto expone los modelos del sistema MNGTournament mediante endpoints RESTful que permiten realizar operaciones CRUD completas sobre organizadores, jugadores, equipos, torneos e inscripciones.

# 👥 Integrantes

- Ronald Wilmer Manrique Supanta
- Manuel Valdivia Flores
- Diego Joaquin Cahuana Vera

---

# 📚 Curso

**Desarrollo de Aplicaciones Web**

Universidad Nacional de San Agustín de Arequipa - UNSA

Semestre Académico 2026-A

---

## 📋 Descripción

Este proyecto extiende la aplicación Django desarrollada en laboratorios anteriores incorporando una API REST que permite el acceso a los datos mediante peticiones HTTP.

La API utiliza:

- Django
- Django REST Framework (DRF)
- ModelViewSet
- ModelSerializer
- DefaultRouter
- Serializadores planos y anidados

## 🎯 Objetivos

- Implementar una API REST utilizando Django REST Framework.
- Exponer los modelos del sistema mediante endpoints REST.
- Implementar serializadores para operaciones CRUD.
- Crear serializadores anidados para consultas detalladas.
- Registrar automáticamente las rutas mediante `DefaultRouter`.
- Validar el funcionamiento utilizando Postman.

---

# 📂 Estructura del Proyecto

```bash
MyDjangoProject/
│
├── MyWebApps/
│   └── MNGTournament/
│       ├── models/
│       ├── serializers/
│       │   ├── OrganizerSerializer.py
│       │   ├── TeamSerializer.py
│       │   ├── PlayerSerializer.py
│       │   ├── TournamentSerializer.py
│       │   ├── PlayerTournamentSerializer.py
│       │   ├── TournamentDetailSerializer.py
│       │   ├── PlayerDetailSerializer.py
│       │   └── PlayerTournamentDetailSerializer.py
│       │
│       ├── views.py
│       ├── urls.py
│       └── admin.py
│
└── manage.py
```

---

# 🛠 Instalación

## 1. Clonar el repositorio

```bash
git clone https://github.com/usuario/MNGTournament.git
cd MNGTournament
```

## 2. Crear entorno virtual

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

## 3. Instalar dependencias

```bash
pip install django
pip install djangorestframework
```

o

```bash
pip install -r requirements.txt
```

---

# ⚙️ Configuración

Agregar Django REST Framework en:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

Configurar permisos:

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}
```

---

# 🗄️ Modelos del Sistema

## Organizer

Representa al organizador de los torneos.

## Player

Representa a los jugadores registrados.

## Team

Representa los equipos participantes.

## Tournament

Representa los torneos deportivos.

## PlayerTournament

Relaciona jugadores con torneos mediante una relación Many-To-Many.

---

# 🔄 Serializadores

## Serializadores Básicos

- OrganizerSerializer
- TeamSerializer
- PlayerSerializer
- TournamentSerializer
- PlayerTournamentSerializer

Utilizados para:

- Listados
- Creación
- Actualización
- Eliminación

---

## Serializadores Anidados

### TournamentDetailSerializer

Incluye los jugadores inscritos en un torneo.

### PlayerDetailSerializer

Incluye los torneos en los que participa un jugador.

### PlayerTournamentDetailSerializer

Devuelve información detallada del jugador y torneo asociados.

---

# 👨‍💻 ViewSets

Cada entidad utiliza un `ModelViewSet` para implementar automáticamente:

- GET
- POST
- PUT
- PATCH
- DELETE

Ejemplo:

```python
class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PlayerDetailSerializer
        return PlayerSerializer
```

---

# 🌐 Endpoints Disponibles

## Organizers

```http
GET     /api/organizers/
POST    /api/organizers/
GET     /api/organizers/{id}/
PUT     /api/organizers/{id}/
DELETE  /api/organizers/{id}/
```

## Teams

```http
GET     /api/teams/
POST    /api/teams/
GET     /api/teams/{id}/
PUT     /api/teams/{id}/
DELETE  /api/teams/{id}/
```

## Players

```http
GET     /api/players/
POST    /api/players/
GET     /api/players/{id}/
PUT     /api/players/{id}/
DELETE  /api/players/{id}/
```

## Tournaments

```http
GET     /api/tournaments/
POST    /api/tournaments/
GET     /api/tournaments/{id}/
PUT     /api/tournaments/{id}/
DELETE  /api/tournaments/{id}/
```

## PlayerTournaments

```http
GET     /api/playertournaments/
POST    /api/playertournaments/
GET     /api/playertournaments/{id}/
PUT     /api/playertournaments/{id}/
DELETE  /api/playertournaments/{id}/
```

---

# 🚀 Ejecución

Aplicar migraciones:

```bash
python manage.py makemigrations
python manage.py migrate
```

Iniciar servidor:

```bash
python manage.py runserver
```

Acceder a:

```text
http://127.0.0.1:8000/api/
```

---

# 🧪 Pruebas con Postman

La API fue validada utilizando Postman mediante operaciones CRUD completas.

Pruebas realizadas:

✅ Crear registros

✅ Consultar registros

✅ Actualizar registros

✅ Eliminar registros

✅ Consultar respuestas JSON anidadas

---

# 📸 Evidencias

- Instalación de Django REST Framework.
- Creación de serializadores.
- Implementación de serializadores anidados.
- Configuración de ViewSets.
- Configuración de rutas mediante DefaultRouter.
- Pruebas realizadas con Postman.

