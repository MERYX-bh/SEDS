from pydantic import BaseModel
import datetime
#Create Pydantic Base models whith common attributes whilecreating or reading data.
class PostBase(BaseModel):
    publishedAt: datetime.datetime
    title: str
    content: str
class UserBase(BaseModel):
    name: str
    email: str
class Post(PostBase):
    id: int
    author: int
    class Config:
        orm_mode = True
class User(UserBase):
    id: int
    class Config:
        orm_mode = True

class PostCreate(PostBase):
    pass
class UserCreate(UserBase):
    posts: list[Post] = []
    pass