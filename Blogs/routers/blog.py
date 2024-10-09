"""
If you are building an application or a web API, it's rarely the case that you can put everything in a single file.
FastAPI provides a convenience tool to structure your application while keeping all the flexibility.

"""
from fastapi import APIRouter, HTTPException, status, Depends, Response
from sqlalchemy.orm import Session
from .. import models,database,schemas
from typing import List
from ..repository import blog

get_db = database.get_db

router = APIRouter(
    prefix='/blog',
    tags=['blogs'])


@router.post('/', status_code = status.HTTP_201_CREATED) #tags are provided to divide the api docs based on the model 
def create(request : schemas.Blog,db : Session = Depends(get_db)):
    return blog.create_blog(request,db)


@router.get('/',status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog]) #response_model helps us to customize the response that we need to return
def all_blogs(db: Session= Depends(get_db)):
    return blog.get_allBlogs(db)
    

@router.get('/{id}/', status_code=status.HTTP_200_OK,response_model=schemas.ShowBlog,)
def blogs(id, response:Response, db: Session = Depends(get_db)):
    return blog.get_blog(id,db)

@router.delete('/{id}/', status_code=status.HTTP_204_NO_CONTENT)
def deleteBlog(id, db:Session = Depends(get_db)):
    return blog.delete_blog(id, db)

@router.put('/{id}/',status_code=status.HTTP_202_ACCEPTED)
def updateBlog(id,request:schemas.Blog, db: Session = Depends(get_db)):
    return blog.update_blog(id,request, db) 

