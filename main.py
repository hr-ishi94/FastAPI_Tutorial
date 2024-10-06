from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data':'blog list'}

@app.get('/blog/unpublished/') #if same route is given for both dynamic and static function always add static route above all the same dynamic ones as to avoid errors
def unpublished():
    return {'data':'unpublished'}


@app.get('/blog/{id}/')
def show(id:int): #providing specific data types in the dynamic routing will only allow the specific datatype otherwise all are considered as strings
    return {'data':id}


@app.get('/about')
def about():

    return 'about hello world'