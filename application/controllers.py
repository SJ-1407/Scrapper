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
#from flask_login import current_user, login_required



'''@app.route("/",methods=["GET","POST"])
def index():
    venue=Venue.query.all()
    if "username" in session and session["user_role"]=='admin':
         return (render_template("admin.html",user=session["username"],role=session["user_role"]))
    elif  "username" in session:

        return render_template("index.html", user = session["username"], signed=True,role=session["user_role"],venue=venue)
    else:
        return render_template("index.html", user = "", signed=False,venue=venue)'''


'''@app.route('/')
def index():
    fetch_hackernews_data(pages=3)  # Call the data fetching script
    news_items = NewsItem.query.filter_by(is_deleted=False).order_by(NewsItem.posted_on.desc()).limit(90).all()
    print("News Items Query:", str(news_items.statement.compile(dialect=db.engine.dialect)))  
    print("News Items:", news_items)  # Add this line for debugging
    return render_template('dashboard.html', news_items=news_items)'''
'''@app.route('/')
def index():
    fetch_hackernews_data(pages=3)  # Call the data fetching script
    news_items_query = NewsItem.query.filter_by(is_deleted=False).order_by(NewsItem.posted_on.desc()).limit(90)
    news_items = news_items_query.all()

    # Print the raw SQL query
    print("News Items Query:", str(news_items_query.statement.compile(dialect=db.engine.dialect)))

    print("News Items:", news_items)  # Add this line for debugging
    return render_template('dashboard.html', news_items=news_items)'''
'''@app.route('/')
def index():
    fetch_hackernews_data(pages=3)  # Call the data fetching script
    news_items_query = NewsItem.query.filter_by(is_deleted=False).order_by(NewsItem.posted_on.desc()).limit(90)
    news_items = news_items_query.all()

    # Print the raw SQL query
    print("News Items Query:", str(news_items_query.statement.compile(dialect=db.engine.dialect)))

    print("News Items:", news_items)  # Add this line for debugging
    return render_template('dashboard.html', news_items=news_items)'''

@app.route('/')
def index():
    fetch_hackernews_data(pages=3)  # Call the data fetching script
    
    # Print the records before the query
    #print("News Items Before Query:", NewsItem.query.all())
    
    news_items_query = NewsItem.query.filter_by(is_deleted=False).order_by(NewsItem.posted_on.desc()).limit(90)
    news_items = news_items_query.all()
    #news_items = NewsItem.query.filter_by(is_deleted=False).order_by(NewsItem.posted_on.desc(), (NewsItem.upvotes).desc()).limit(90).all()

    # Print the raw SQL query
    #print("News Items Query:", str(news_items_query.statement.compile(dialect=db.engine.dialect)))

    #print("News Items:", news_items)  # Add this line for debugging
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
               session["username"]=username  #maintaining cookie
               session["user_email"]=user.email
               return redirect(url_for("login"))
        else:
           error = "Enter a valid email"
           return render_template("register_user.html", error = error)
        
@app.route("/logout")
def logout():
    if "username" in session:
        session.pop("username")
        session.pop("user_email")
    return redirect("/")
'''from flask import redirect, render_template, request, session, url_for, flash
from flask_bcrypt import check_password_hash, generate_password_hash

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        if "username" in session:
            return redirect(url_for("index"))
        error_message = request.args.get("error")
        return render_template("login.html", error_message=error_message)
    elif request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        # Check if the user exists
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            session["username"] = user.username
            session["user_email"] = user.email
            flash("Login successful!", "success")
            return redirect(url_for('index'))
        else:
            flash("Invalid email or password.", "error")
            return render_template('login.html')

    # If none of the conditions are met, return an error response
    flash("Invalid request.", "error")
    return render_template('login.html')


@app.route("/register", methods=["GET", "POST"])
def register():
    if "username" in session:
        return redirect(url_for("index"))

    if request.method == 'GET':
        return render_template("register_user.html")
    elif request.method == 'POST':
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        if "@" in email:
            user = User.query.filter_by(email=email).first()

            if user:
                flash("Email already registered", "error")
                return render_template("register_user.html")

            if password != request.form["confirm_password"]:
                flash("Password does not match with Confirm Password", "error")
                return render_template("register_user.html")

            password_hash = generate_password_hash(password).decode('utf-8')
            new_user = User(username=username, email=email, password=password_hash)

            db.session.add(new_user)
            db.session.commit()

            session["username"] = username
            session["user_email"] = email
            flash("Registration successful! You are now logged in.", "success")
            return redirect(url_for("index"))
        else:
            flash("Enter a valid email", "error")
            return render_template("register_user.html")

@app.route("/logout")
def logout():
    if "username" in session:
        session.pop("username")
        session.pop("user_email")
        flash("Logged out successfully!", "success")
    return redirect("/")

'''

@app.route('/update_data')
def update_data():
    fetch_hackernews_data(pages=3)
    return 'Data updated successfully'

@app.route('/mark_as_read/<int:news_id>')
#@login_required
def mark_as_read(news_id):
    news_item = NewsItem.query.get(news_id)

    if news_item:
        news_item.is_read = True
        db.session.commit()

    return redirect(url_for('index'))

@app.route('/delete_news/<int:news_id>')
#@login_required
def delete_news(news_id):
    news_item = NewsItem.query.get(news_id)

    if news_item:
        news_item.is_deleted = True
        db.session.commit()

    return redirect(url_for('index'))


