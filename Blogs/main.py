from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas,models
from sqlalchemy.orm import Session
from .database import engine,SessionLocal

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

@app.post('/blog', status_code = status.HTTP_201_CREATED)
def create(request : schemas.Blog,db : Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title, body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blogs',status_code=status.HTTP_200_OK)
def all_blogs(db: Session= Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}/', status_code=status.HTTP_200_OK)
def blog(id, response:Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail':f'blog with id {id} not found'}  ## HTTPException can be used to replace all these two line of codes
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not found")  
    return blog

@app.delete('/blog/{id}/', status_code=status.HTTP_204_NO_CONTENT)
def deleteBlog(id, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail= f'Blog of id {id} is not found')
    blog.delete(synchronize_session = False)
    db.commit()
    return " Blog is deleted "

@app.put('/blog/{id}/',status_code=status.HTTP_202_ACCEPTED)
def updateBlog(id,request:schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f" Blog with id {id} is not found")
    blog.update({"title":request.title,'body':request.body})
    db.commit()
    # db.refresh(blog)
    return "blog"