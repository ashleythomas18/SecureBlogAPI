from fastapi import FastAPI,status
from .database import engine
from . import models,schemas
import uvicorn
from pydantic import BaseModel
from . import hashing
from .routers import blog,user,authentication


app= FastAPI()

models.Base.metadata.create_all(bind=engine) #the reason tableplus pr tables shpw horhi hai
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

models.Base.metadata.create_all(engine)






'''@app.get("/blog")
def index(limit=10, published:bool=True,sort: Optional[str]= None):
    

    if published:
        return {'data':f'{limit} published blogs from the db'}
    else:
        return {'data':f'{limit} blogs from the db'}'''

    #only get 10 published blogs
    #return {'data':f'{limit} blogs from the db'}

# @app.get('/blog/unpublished')

# def unpublished():
#     return {'data': 'all unpublished blogs'}


# @app.get("/blog/{id}")
# def show(id: int):

#     #fetch blog woth id=id
#     return{'data':id}


# @app.get('/blog/{id}/comments')
# def comments(id,limit=10):
    
#     return{'data':{1,2}}







@app.post('/blog', tags=['blogs'])

def create_blog(request: schemas.Blog):
    
    return {'data': f'Blog is created with title  {request.title}'}
    
# if __name__== "__main__":
#    uvicorn.run(app,host="127.0.0.1", port=8000)


