from flask import Flask, request,redirect,url_for,session
from flask import render_template
from flask import current_app as app
from application.database import db
from flask_sqlalchemy import SQLAlchemy
from application.models import *
from flask_bcrypt import Bcrypt
bcrypt=Bcrypt(app)
from retrieve import fetch_hackernews_data
from sqlalchemy import text 
from flask import flash



@app.route('/')
def index():
    fetch_hackernews_data(pages=3)  
    
  
    news_items_query = NewsItem.query.filter_by(is_deleted=False).order_by(NewsItem.posted_on.desc()).limit(90)
    news_items = news_items_query.all()
   
    return render_template('dashboard.html', news_items=news_items)

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
      if "username" in session:
         return(redirect(url_for("index")))
      error_message=request.args.get("error")  
      return (render_template("login.html",error_message=error_message))
    else:
     if request.method=="POST":
        user=User.query.filter_by(email=request.form["email"]).first()
   
        if user:
            if bcrypt.check_password_hash(user.password,request.form["password"]):
                session["user_id"] = user.id
                session["username"]= user.username
                session["user_email"]=user.email
                return redirect(url_for('index'))
            else:
              error_message = "Invalid email or password."
              return render_template('login.html', error_message=error_message)
        else:
            return (render_template("login.html",error_message="Invalid User/Password"))
           

      



@app.route("/register",methods=["GET","POST"])
def register():
    if "username" in session:
         return(redirect(url_for("index")))
    if request.method=='GET':
     return (render_template("register_user.html"))
    elif request.method=='POST':
        username=request.form["username"]
        email = request.form["email"]
        if "@" in email:
            user=User.query.filter_by(email=request.form["email"]).first()
            password=request.form["password"]
            if user:
               error="Email already registered"
               return (render_template("register_user.html", error=error))
            else:
               if(password!=request.form["confirm_password"]):
                  error="Password does not match with Confirm Password"
                  return(render_template("register_user.html",error=error))
               password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
              
              
               user=User(username=username,email=email,password=password_hash)
        
               db.session.add(user)
               db.session.commit()
               session["user_id"] = user.id
               session["username"]=username  #maintaining cookie
               session["user_email"]=user.email
               return redirect(url_for("login"))
        else:
           error = "Enter a valid email"
           return render_template("register_user.html", error = error)


@app.route("/logout")
def logout():
    if "user_id" in session:
        user_id = session["user_id"]
        session.pop("user_id")
        session.pop("username")
        session.pop("user_email")

     
        reset_user_actions(user_id)

    return redirect("/")

def reset_user_actions(user_id):
    
    read_news_items = NewsItem.query.filter_by( is_read=True).all()
    for news_item in read_news_items:
        news_item.is_read = False

    
    deleted_news_items = NewsItem.query.filter_by(is_deleted=True).all()
    for news_item in deleted_news_items:
        news_item.is_deleted = False

    db.session.commit()

@app.route('/update_data')
def update_data():
    fetch_hackernews_data(pages=3)
    return 'Data updated successfully'

@app.route('/mark_as_read/<int:news_id>')

def mark_as_read(news_id):
  if "username" in session:
    news_item = NewsItem.query.get(news_id)

    if news_item:
        news_item.is_read = True
        db.session.commit()

  return redirect(url_for('index'))

@app.route('/delete_news/<int:news_id>')

def delete_news(news_id):
   if "username" in session:
    news_item = NewsItem.query.get(news_id)

    if news_item:
        news_item.is_deleted = True
        db.session.commit()

   return redirect(url_for('index'))

