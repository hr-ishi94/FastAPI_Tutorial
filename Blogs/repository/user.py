from fastapi import HTTPException, status
from .. import schemas, models, hashing
from sqlalchemy.orm import Session

def create_user(request:schemas.User, db:Session):
    hashed_pwd = hashing.hash_pwd(request.password)
    new_user = models.User(name = request.name, email = request.email, password = hashed_pwd)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_allUsers(db:Session):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No users found!")
    return users


def get_user(id:int, db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f" User with the id {id} does not exist.")
    return user