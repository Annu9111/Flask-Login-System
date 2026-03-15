from flask import Flask,request
app=Flask(__name__)
@app.route("/")
def home():
    return "Hello User!!\n This is a Flask app"

@app.route("/about")
def about():
    return "this is about page"

@app.route("/contact")
def contact():
    return "this is contact page"

@app.route("/submit",methods=["GET","POST"])
def submit():
    if request.method=="POST":
        return "You Send Data"
    else:
        return "You are only viewing the form"        
         