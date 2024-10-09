from fastapi import APIRouter, status, Depends,HTTPException
from typing import List
from .. import schemas, database, models, hashing
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(
    prefix='/user',
    tags=['user']
)

get_db = database.get_db

@router.post('/',status_code=status.HTTP_201_CREATED)
def create_user(request:schemas.User, db :Session = Depends(get_db)):
    return user.create_user(request, db)


@router.get('/',status_code=status.HTTP_200_OK,response_model=List[schemas.ShowUser])
def allUsers(db:Session = Depends(get_db)):
    return user.get_allUsers(db)

@router.get('/{id}',status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def get_user(id,db:Session = Depends(get_db)):
    return user.get_user(id, db)
