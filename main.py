from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Blog(BaseModel): # importing Basemodel makes the Blog class as model 
    name:str
    body: str
    published:Optional[bool]


@app.get('/blog')                         #queryparameters  ===>   #http://localhost:8000/blog?limit=50&unpublished=true 
def index(limit = 10,published:bool= False, sort:Optional[str]=None): #will also be able to assign default values and also datatypes for the query parameters
    if published:                                       #Optional is used for providing when sort is not always required even without a default value
        return {'data':f'{limit} published blog list'}
    else:
        return {'data':'No unpublished found'}

@app.get('/blog/unpublished/') #if same route is given for both dynamic and static function always add static route above all the same dynamic ones as to avoid errors
def unpublished():
    return {'data':'unpublished'}


@app.get('/blog/{id}/') #id is a "path parameter" and is determined by checking if it is in the path other wise it will be considered as query parameter
def show(id:int): #providing specific data types in the dynamic routing will only allow the specific datatype otherwise all are considered as strings
    return {'data':id}


@app.post('/blog')
def post(blog:Blog): # "blog" will be considered as the instance of the Pydantic model "Blog"
    return f'New blog name is {blog.name}'