# FastAPI + PostgreSQL con Docker

Este proyecto es una aplicación **FastAPI** que utiliza **PostgreSQL** como base de datos y está dockerizada con **Docker Compose**.

## **1. Requisitos Previos**

Asegúrate de tener instalados los siguientes programas:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python 3.10+](https://www.python.org/downloads/)

## **2. Instalación**

Clona el repositorio en tu equipo local:

```sh
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
```

Crea un archivo `.env` con la configuración de la base de datos:

```sh
touch .env
```

Abre el archivo `.env` y agrega lo siguiente:

```
SECRET_KEY = "secret_key_123456"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
DATABASE_URL = "postgresql://danielcontreras:123456@localhost:5432/energy"
```

## **3. Construcción y Ejecución con Docker**

Ejecuta los siguientes comandos para construir y correr los contenedores:

```sh
docker-compose up --build -d
```

Para verificar que los contenedores están corriendo:

```sh
docker ps
```

## **4. Acceder a la Aplicación**

Una vez que los contenedores estén en ejecución, accede a la API en tu navegador o en Postman:

🔗 [http://localhost:8000/docs](http://localhost:8000/docs)\
Aquí podrás probar los endpoints disponibles con la interfaz interactiva de Swagger.

## **5. Detener los Contenedores**

Si deseas detener los contenedores, ejecuta:

```sh
docker-compose down
```

## **6. Migraciones de la Base de Datos**

Si agregas nuevos modelos a la base de datos, debes ejecutar las migraciones manualmente:

```sh
docker exec -it fastapi_container alembic upgrade head
```

## **7. Notas Adicionales**

- Si realizas cambios en el código, vuelve a construir la imagen con:
  ```sh
  docker-compose up --build -d
  ```
- Si necesitas ver logs de la aplicación en tiempo real:
  ```sh
  docker logs -f fastapi_container
  ```

## **8. Tecnologías Utilizadas**

- **FastAPI** - Framework para APIs en Python
- **PostgreSQL** - Base de datos relacional
- **SQLAlchemy** - ORM para Python
- **Docker & Docker Compose** - Contenerización de la aplicación
- **Uvicorn** - Servidor ASGI

---

### 🚀 **¡Listo! Tu aplicación FastAPI con PostgreSQL está corriendo con Docker.**

