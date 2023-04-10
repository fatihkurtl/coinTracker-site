from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import Flask
from sqlalchemy.sql import func

Base = declarative_base()


class Admin(Base):
    __tablename__ = "admins"
    id = Column(Integer, primary_key = True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    posts = relationship("Post", back_populates="admin")
    
class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String(250))
    content = Column(String(900))
    image = Column(String(250))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    admin_id = Column(Integer, ForeignKey('admins.id'))
    admin = relationship("Admin", back_populates="posts")
    comments = relationship('Comments', back_populates='post')
    

class Users(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key = True)
    fullName = Column(String(100), nullable = False)
    email = Column(String(150), nullable = False, unique = True)
    userName = Column(String(100), nullable = False,  unique = True)
    password = Column(String(300), nullable = False)
    registerTime = Column(DateTime, default = datetime.now)
    
    favoriteCoins = relationship("FavoriteList", back_populates = "user")
    comment = relationship('Comments', back_populates = "user")
    contact = relationship("Contact", back_populates = "user")
    
class FavoriteList(Base):
    __tablename__ = "favoriteCoins"
    
    id = Column(Integer, primary_key = True)
    coinName = Column(String(300), nullable = False)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    user = relationship("Users", back_populates = "favoriteCoins")
    
class Comments(Base):
    __tablename__ = "comments"
    
    id = Column(Integer, primary_key=True)
    content = Column(String(900))
    user_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("posts.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    user = relationship('Users', back_populates='comment')
    post = relationship('Post', back_populates='comments')
    
class Contact(Base):
    __tablename__ = "contact"
    
    id = Column(Integer, primary_key = True)
    fullName = Column(String(100), nullable = False)
    email = Column(String(150), nullable = False)
    phone = Column(String(100), nullable = False)
    message = Column(String(300), nullable = False)
    user_id = Column(Integer, ForeignKey("users.id"))
    sendTime = Column(DateTime, default = datetime.now)
    
    user = relationship("Users", back_populates = "contact")

    
engine = create_engine('mysql://root:2410@localhost/coinTracker', echo=True)
Base.metadata.create_all(engine)