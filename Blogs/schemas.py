from pydantic import BaseModel
from typing import List


class User(BaseModel):
    name: str
    email : str
    password :str

    class Config():
        orm_mode = True

class BaseBlog(BaseModel):
    title : str
    body  : str
    user_id : int
    
class Blog(BaseBlog):
     
    class Config: #Config class is used to provide configurations to Pydantic.
        orm_mode = True #orm_mode will tell the Pydantic model to read the data even if it is not a dict, but an ORM model 


class ShowUser(BaseModel):
    name :str
    email :str
    blogs : List[Blog] = []

    class Config:
        orm_mode = True


class ShowBlog(BaseModel): #for providing custom response 
    title : str
    body :str
    user : ShowUser


    class Config():
        orm_mode = True


class Login(BaseModel):
    username :str
    password : str
