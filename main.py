from fastapi import FastAPI

app = FastAPI()

@app.get('/blog')                         #queryparameters  ===>   #http://localhost:8000/blog?limit=50&unpublished=true 
def index(limit = 10,published:bool= False): #will also be able to assign default values and also datatypes for the query parameters
    if published:
        return {'data':f'{limit} published blog list'}
    else:
        return {'data':'No unpublished found'}

@app.get('/blog/unpublished/') #if same route is given for both dynamic and static function always add static route above all the same dynamic ones as to avoid errors
def unpublished():
    return {'data':'unpublished'}


@app.get('/blog/{id}/')
def show(id:int): #providing specific data types in the dynamic routing will only allow the specific datatype otherwise all are considered as strings
    return {'data':id}


@app.get('/about')
def about():

    return 'about hello world'