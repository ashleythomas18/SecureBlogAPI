from typing import Optional, List
from pydantic import BaseModel

class BlogBase(BaseModel):
    title: str
    body: str
    published: Optional[bool]
    
class Blog(BlogBase):
    class Config:         #to hide the unnecessary details such as user_id or id,
        orm_mode=True     #put the class config for this purpose.


class User(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        from_attributes=True

class ShowUser(BaseModel):
    name: str
    email: str
    blog: List[Blog]=[]

    class Config:
        orm_mode=True

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser
    class Config():
        orm_mode= True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None