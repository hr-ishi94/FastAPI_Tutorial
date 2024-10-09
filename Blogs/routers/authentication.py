from fastapi import APIRouter,Depends,status, HTTPException
from .. import schemas,database,models, hashing
from sqlalchemy.orm import Session


router= APIRouter(prefix='/login' , tags=['Authentication'])

@router.post('/',status_code=status.HTTP_200_OK)
def login(request:schemas.Login,db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials!")
    if not hashing.hash_verify(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect Password!")
    return user        