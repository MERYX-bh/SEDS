from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Column, ForeignKey,Integer, String, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
#Create a Base class using declarative_base(). Used to
Base = declarative_base()
class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True,
    autoincrement = True)
    publishedAt = Column(DateTime(timezone=True),
    nullable=True, server_default=func.now())
    title = Column(String, index=True, nullable=False)
    content = Column(Text, nullable=False)
    author = Column(Integer, ForeignKey("users.id"))
    #Establish a bidirectional One-To-Mant relationship
    owner = relationship("User", back_populates="posts")
    
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True,
    autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    #Establish a bidirectional One-To-Many relationship
    posts = relationship("Post", back_populates="owner")