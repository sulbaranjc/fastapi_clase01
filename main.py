from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from uuid import uuid4 as uuid
from typing import Optional, Text

app = FastAPI()

posts = []

# Post Model
class Post(BaseModel):
    id: Optional[str]
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime] = None
    published: bool = False

class PostUpdate(BaseModel):
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()

@app.get('/')
def read_root():
    return {'Welcome': 'Bienvenido a mi Blog'}

@app.get('/posts')
def get_posts():
    return posts

@app.post('/posts/create')
def create_post(post:Post):
    post.id = str(uuid())
    posts.append(post.dict())
    return {'message':'Post creado satisfactoriamente'}

@app.get('/posts/{post_id}')
def get_post_by_id(post_id:str):
    for post in posts:
        if post['id'] == post_id:
            return post
    raise HTTPException(status_code=404, detail='Post no encontrado')

@app.delete('/posts/delete/{post_id}')
def delete_post(post_id:str):
    for index, post in enumerate(posts):
        if post['id'] == post_id:
            posts.pop(index)
            return {'message':'Post eliminado correctamente'}
    raise HTTPException(status_code=404, detail='Post no encontrado')

@app.put('/posts/update/{post_id}')
def update_post(post_id:str, updatedPost:PostUpdate):
    for post in posts:
        if post['id'] == post_id:
            post.update(updatedPost.dict())
            return {'message':'Post actualizado correctamente'}
    raise HTTPException(status_code=404, detail='Post no encontrado')
