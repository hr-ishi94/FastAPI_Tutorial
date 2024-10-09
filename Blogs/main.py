from fastapi import FastAPI
from . import models
from .database import engine
from .routers import user,blog,authentication

app = FastAPI()


# models.Base.metadata.drop_all(bind=engine, tables=[models.Base.metadata.tables['users']]) #Can be used to drop the table 
# models.Base.metadata.drop_all(bind=engine, tables=[models.Base.metadata.tables['blogs']])

models.Base.metadata.create_all(bind=engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)

