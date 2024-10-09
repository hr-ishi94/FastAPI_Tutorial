from fastapi import HTTPException,status
from .. import schemas, models
from sqlalchemy.orm import Session

def get_allBlogs(db:Session):
    blogs = db.query(models.Blog).all()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "No Blogs found!")
    return blogs

def get_blog(id:int,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail':f'blog with id {id} not found'}  # HTTPException can be used to replace all these two line of codes
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not found")  
    return blog

def create_blog(request:schemas.Blog,db:Session):
    user = db.query(models.User).filter(models.User.id == request.user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"User with id {request.user_id} is not found. Failed to post a new blog")
    
    new_blog = models.Blog(title = request.title, body = request.body, user_id=request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete_blog(id:int,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail= f'Blog of id {id} is not found')
    blog.delete(synchronize_session = False)
    db.commit()
    return {"detail":" Blog is deleted "}

def update_blog(id:int,request:schemas.Blog ,db:Session):
    blog_query = db.query(models.Blog).filter(models.Blog.id == id)
    blog = blog_query.first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f" Blog with id {id} is not found")
    blog_query.update({"title": request.title, "body": request.body, "user_id": request.user_id})
    
    db.commit()

    # Retrieve the updated blog instance
    updated_blog = blog_query.first()
    db.refresh(updated_blog)  # Refresh the updated instance

    return updated_blog  