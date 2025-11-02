# ============================================================================
# EJEMPLO BÁSICO DE API REST CON FASTAPI
# ============================================================================
# Este archivo demuestra cómo crear una API REST básica para un blog
# utilizando FastAPI, uno de los frameworks más populares de Python

# IMPORTACIONES NECESARIAS
# ============================================================================

# FastAPI: Framework principal para crear APIs REST modernas y rápidas
# HTTPException: Para manejar errores HTTP de manera elegante
from fastapi import FastAPI, HTTPException

# BaseModel: Clase base de Pydantic para crear modelos de datos con validación automática
from pydantic import BaseModel

# Para trabajar con fechas y timestamps
from datetime import datetime

# Para generar identificadores únicos (UUID) para nuestros posts
from uuid import uuid4 as uuid

# Tipos de datos especiales para hacer el código más legible y seguro
from typing import Optional, Text

# INICIALIZACIÓN DE LA APLICACIÓN FASTAPI
# ============================================================================
# Creamos la instancia principal de nuestra aplicación
# FastAPI() crea automáticamente documentación interactiva en /docs
app = FastAPI()

# BASE DE DATOS EN MEMORIA (SIMULADA)
# ============================================================================
# En un proyecto real, esto sería una base de datos como PostgreSQL, MySQL, etc.
# Para este ejemplo didáctico, usamos una lista simple en memoria
posts = []

# MODELOS DE DATOS (SCHEMAS)
# ============================================================================
# Los modelos definen la estructura de los datos que acepta nuestra API
# Pydantic se encarga automáticamente de validar que los datos cumplan estas reglas


# Modelo principal para crear y representar un post del blog
class Post(BaseModel):
    id: Optional[str]  # ID único, se genera automáticamente, por eso es opcional
    title: str  # Título del post (obligatorio)
    author: str  # Autor del post (obligatorio)
    content: Text  # Contenido del post (texto largo, obligatorio)
    created_at: datetime = datetime.now()  # Fecha de creación (automática)
    published_at: Optional[datetime] = None  # Fecha de publicación (opcional)
    published: bool = False  # Estado de publicación (por defecto no publicado)


# Modelo específico para actualizaciones
# Separamos este modelo para tener más control sobre qué campos se pueden actualizar
class PostUpdate(BaseModel):
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()


# ENDPOINTS DE LA API (RUTAS)
# ============================================================================
# Los endpoints definen las URLs y métodos HTTP que acepta nuestra API


# ENDPOINT RAÍZ - GET /
# ============================================================================
# Decorador @app.get: Define una ruta que responde a peticiones GET
# El '/' indica que es la ruta raíz de nuestra API (ejemplo: http://localhost:8000/)
@app.get("/")
def read_root():
    """
    Endpoint de bienvenida - Punto de entrada principal de la API

    Returns:
        dict: Mensaje de bienvenida en formato JSON
    """
    return {"Welcome": "Bienvenido a mi Clase de FastAPI"}


# OBTENER TODOS LOS POSTS - GET /posts
# ============================================================================
@app.get("/posts")
def get_posts():
    """
    Obtiene todos los posts del blog

    Returns:
        list: Lista con todos los posts almacenados en memoria

    Ejemplo de uso:
        GET http://localhost:8000/posts
    """
    return posts


# CREAR NUEVO POST - POST /posts/create
# ============================================================================
@app.post("/posts/create")
def create_post(post: Post):
    """
        Crea un nuevo post en el blog

        Args:
            post (Post): Objeto Post con los datos del nuevo post
                        FastAPI automáticamente valida que los datos cumplan el modelo

        Returns:
            dict: Mensaje de confirmación

        Ejemplo de uso:
            POST http://localhost:8000/posts/create
            Body (JSON):
    {
      "id": "art-20251102-001",
      "title": "Cómo crear un monolito Python con FastAPI y Jinja2 paso a paso",
      "author": "Juan Carlos Sulbarán González",
      "content": "En este artículo exploraremos cómo montar un monolito web en Python utilizando FastAPI y Jinja2. Veremos cómo estructurar las carpetas, crear rutas GET y POST, validar formularios tanto en el frontend como en el backend, y finalmente desplegar el proyecto en un entorno local con Uvicorn. Este enfoque didáctico está pensado para estudiantes de FP en Desarrollo de Aplicaciones Web y Multiplataforma.",
      "created_at": "2025-11-02T21:39:47.784832",
      "published_at": "2025-11-02T22:00:00.000Z",
      "published": true
    }
    """
    # Generamos un ID único para el post
    post.id = str(uuid())

    # Convertimos el objeto Pydantic a diccionario y lo agregamos a nuestra "base de datos"
    posts.append(post.model_dump())

    return {"message": "Post creado satisfactoriamente"}


# OBTENER POST POR ID - GET /posts/{post_id}
# ============================================================================
@app.get("/posts/{post_id}")
def get_post_by_id(post_id: str):
    """
    Obtiene un post específico por su ID único

    Args:
        post_id (str): ID único del post que queremos obtener
                      Se extrae automáticamente de la URL

    Returns:
        dict: Los datos del post encontrado

    Raises:
        HTTPException: Error 404 si el post no existe

    Ejemplo de uso:
        GET http://localhost:8000/posts/abc-123-def-456
    """
    # Buscamos el post en nuestra lista
    for post in posts:
        if post["id"] == post_id:
            return post

    # Si no encontramos el post, lanzamos una excepción HTTP 404
    raise HTTPException(status_code=404, detail="Post no encontrado")


# ELIMINAR POST - DELETE /posts/delete/{post_id}
# ============================================================================
@app.delete("/posts/delete/{post_id}")
def delete_post(post_id: str):
    """
    Elimina un post específico por su ID

    Args:
        post_id (str): ID único del post que queremos eliminar

    Returns:
        dict: Mensaje de confirmación de eliminación

    Raises:
        HTTPException: Error 404 si el post no existe

    Ejemplo de uso:
        DELETE http://localhost:8000/posts/delete/abc-123-def-456
    """
    # enumerate() nos da tanto el índice como el valor en cada iteración
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            # pop() elimina el elemento en la posición indicada
            posts.pop(index)
            return {"message": "Post eliminado correctamente"}

    # Si llegamos aquí, el post no fue encontrado
    raise HTTPException(status_code=404, detail="Post no encontrado")


# ACTUALIZAR POST - PUT /posts/update/{post_id}
# ============================================================================
@app.put("/posts/update/{post_id}")
def update_post(post_id: str, updatedPost: PostUpdate):
    """
    Actualiza un post existente con nuevos datos

    Args:
        post_id (str): ID único del post que queremos actualizar
        updatedPost (PostUpdate): Nuevos datos para el post
                                 FastAPI valida automáticamente este objeto

    Returns:
        dict: Mensaje de confirmación de actualización

    Raises:
        HTTPException: Error 404 si el post no existe

    Ejemplo de uso:
        PUT http://localhost:8000/posts/update/abc-123-def-456
        Body (JSON):
        {
            "title": "Título actualizado",
            "author": "Autor actualizado",
            "content": "Contenido actualizado..."
        }
    """
    # Buscamos el post que queremos actualizar
    for post in posts:
        if post["id"] == post_id:
            # update() fusiona los nuevos datos con los existentes
            # model_dump() convierte el objeto Pydantic a diccionario
            post.update(updatedPost.model_dump())
            return {"message": "Post actualizado correctamente"}

    # Si el post no existe, lanzamos error 404
    raise HTTPException(status_code=404, detail="Post no encontrado")


# ============================================================================
# NOTAS IMPORTANTES PARA ESTUDIANTES:
# ============================================================================
#
# 1. MÉTODOS HTTP utilizados:
#    - GET: Para obtener datos (lectura)
#    - POST: Para crear nuevos recursos
#    - PUT: Para actualizar recursos existentes
#    - DELETE: Para eliminar recursos
#
# 2. CÓDIGOS DE ESTADO HTTP:
#    - 200: OK (operación exitosa)
#    - 404: Not Found (recurso no encontrado)
#    - 422: Unprocessable Entity (datos inválidos - automático con Pydantic)
#
# 3. VALIDACIÓN AUTOMÁTICA:
#    FastAPI + Pydantic validan automáticamente los datos de entrada
#    Si los datos no cumplen el modelo, se devuelve error 422
#
# 4. DOCUMENTACIÓN AUTOMÁTICA:
#    Visita http://localhost:8000/docs para ver la documentación interactiva
#    También disponible en formato ReDoc en http://localhost:8000/redoc
#
# 5. PARA EJECUTAR ESTA API:
#    uvicorn main:app --reload
#    Esto iniciará el servidor en http://localhost:8000
#
# ============================================================================
