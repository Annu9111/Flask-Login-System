from flask import Flask
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