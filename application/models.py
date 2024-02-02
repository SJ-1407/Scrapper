from application.database import db
from flask_sqlalchemy import SQLAlchemy






class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    username = db.Column(db.String, unique=False,nullable=False)
    email = db.Column(db.String, unique=True,nullable=False)
    password = db.Column(db.String(255),nullable=False)
   
    

class NewsItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))  
    url = db.Column(db.String(255))
    hacker_news_url = db.Column(db.String(255), unique=True)
    posted_on = db.Column(db.DateTime)
    upvotes = db.Column(db.Integer)
    comments = db.Column(db.Integer)
    is_read = db.Column(db.Boolean, default=False)
    is_deleted = db.Column(db.Boolean, default=False)
   


