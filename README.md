# 📚 FastAPI - Ejemplo Básico para Estudiantes

## 🎯 Descripción del Proyecto

Este proyecto es un **ejemplo didáctico** para aprender a desarrollar APIs REST con **FastAPI**, uno de los frameworks más modernos y eficientes de Python. 

La aplicación implementa un **blog básico** con operaciones CRUD (Create, Read, Update, Delete) para gestionar posts, demostrando los conceptos fundamentales del desarrollo de APIs.

## 🚀 ¿Qué es FastAPI?

**FastAPI** es un framework web moderno y rápido para construir APIs con Python basado en las anotaciones de tipos estándar de Python. Sus principales características son:

- ⚡ **Muy rápido**: Uno de los frameworks más rápidos disponibles
- 📖 **Documentación automática**: Genera documentación interactiva automáticamente
- 🔍 **Validación automática**: Valida datos usando Pydantic
- 🐍 **Moderno**: Aprovecha las características más recientes de Python
- 🛡️ **Seguro**: Incluye características de seguridad por defecto

## 🛠️ Instalación y Configuración

### Prerrequisitos
- Python 3.7+ instalado en tu sistema
- pip (gestor de paquetes de Python)

### 1. Clonar o descargar el proyecto
```bash
# Si tienes Git instalado
git clone https://github.com/sulbaranjc/fastapi_clase01.git
cd fastapi_clase01

# O simplemente descarga los archivos del proyecto
```

### 2. Crear un entorno virtual (recomendado)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar las dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación
```bash
uvicorn main:app --reload
```

¡Listo! Tu API estará disponible en: **http://localhost:8000**

## 📋 Estructura del Proyecto

```
fastapi/
│
├── main.py              # Archivo principal con la lógica de la API
├── requirements.txt     # Dependencias del proyecto
├── README.md           # Este archivo
└── __pycache__/        # Cache de Python (generado automáticamente)
```

## 🌐 Endpoints Disponibles

### 📖 Documentación Interactiva
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### 🔗 Rutas de la API

| Método | Ruta | Descripción | Ejemplo |
|--------|------|-------------|---------|
| `GET` | `/` | Mensaje de bienvenida | `http://localhost:8000/` |
| `GET` | `/posts` | Obtener todos los posts | `http://localhost:8000/posts` |
| `POST` | `/posts/create` | Crear un nuevo post | `http://localhost:8000/posts/create` |
| `GET` | `/posts/{post_id}` | Obtener post por ID | `http://localhost:8000/posts/abc-123` |
| `PUT` | `/posts/update/{post_id}` | Actualizar un post | `http://localhost:8000/posts/update/abc-123` |
| `DELETE` | `/posts/delete/{post_id}` | Eliminar un post | `http://localhost:8000/posts/delete/abc-123` |

## 📝 Ejemplos de Uso

### 1. Crear un nuevo post
```bash
# Usando curl
curl -X POST "http://localhost:8000/posts/create" \
     -H "Content-Type: application/json" \
     -d '{
       "title": "Mi primer post",
       "author": "Estudiante ILERNA",
       "content": "Este es mi primer post usando FastAPI. ¡Está genial!"
     }'
```

### 2. Obtener todos los posts
```bash
curl -X GET "http://localhost:8000/posts"
```

### 3. Obtener un post específico
```bash
curl -X GET "http://localhost:8000/posts/{post_id}"
```

### 4. Actualizar un post
```bash
curl -X PUT "http://localhost:8000/posts/update/{post_id}" \
     -H "Content-Type: application/json" \
     -d '{
       "title": "Título actualizado",
       "author": "Autor actualizado",
       "content": "Contenido actualizado del post"
     }'
```

### 5. Eliminar un post
```bash
curl -X DELETE "http://localhost:8000/posts/delete/{post_id}"
```

## 🎓 Conceptos Aprendidos

### 🔧 Tecnologías Utilizadas
- **FastAPI**: Framework principal para crear la API
- **Pydantic**: Validación y serialización de datos
- **Uvicorn**: Servidor ASGI para ejecutar la aplicación
- **Python Type Hints**: Anotaciones de tipos para mejor código

### 📚 Conceptos de APIs REST
- **Métodos HTTP**: GET, POST, PUT, DELETE
- **Códigos de estado**: 200 (OK), 404 (Not Found), 422 (Validation Error)
- **Rutas parametrizadas**: `/posts/{post_id}`
- **Validación de datos**: Automática con Pydantic
- **Serialización JSON**: Conversión automática de objetos Python

### 🏗️ Patrones de Diseño
- **Modelos de datos**: Separación entre `Post` y `PostUpdate`
- **Manejo de errores**: Uso de `HTTPException`
- **Documentación**: Docstrings y comentarios explicativos

## 🚨 Importante para Estudiantes

### ⚠️ Limitaciones de este ejemplo
- **Base de datos en memoria**: Los datos se pierden al reiniciar la aplicación
- **Sin persistencia**: En un proyecto real usarías PostgreSQL, MySQL, etc.
- **Sin autenticación**: No hay sistema de usuarios o permisos
- **Sin validaciones avanzadas**: Ejemplo básico para aprendizaje

### 🎯 Próximos pasos sugeridos
1. Agregar una base de datos real (SQLAlchemy + PostgreSQL)
2. Implementar autenticación y autorización
3. Agregar más validaciones a los modelos
4. Implementar paginación para los posts
5. Agregar pruebas unitarias
6. Desplegar en la nube (Heroku, Railway, etc.)

## 🛠️ Dependencias del Proyecto

```
fastapi==0.104.1        # Framework principal
uvicorn[standard]==0.24.0  # Servidor ASGI
pydantic==2.5.0         # Validación de datos
```

## 🐛 Solución de Problemas Comunes

### Error: "ModuleNotFoundError"
```bash
# Asegúrate de haber instalado las dependencias
pip install -r requirements.txt
```

### Error: "Port already in use"
```bash
# Cambia el puerto si el 8000 está ocupado
uvicorn main:app --reload --port 8001
```

### La aplicación no recarga automáticamente
```bash
# Asegúrate de usar la opción --reload
uvicorn main:app --reload
```

## 📞 Soporte y Contacto

- **Profesor**: Juan Carlos Sulbarán
- **Institución**: ILERNA
- **Curso**: CMO Programación en Python 2025-2026

## 📄 Licencia

Este proyecto es con fines educativos para los estudiantes de ILERNA.

---

### 🎉 ¡Felicitaciones!

Si has llegado hasta aquí y has logrado ejecutar la aplicación, ¡has dado tus primeros pasos en el desarrollo de APIs con FastAPI! 

**Continúa practicando y experimentando con el código.** 🚀

---

**Desarrollado con ❤️ para los estudiantes de ILERNA**