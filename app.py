from flask import Flask,request,redirect,url_for,session,Response

app=Flask(__name__)

#homepage or login page
@app.route("/",methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        
        if username=="admin" and password=="123":
            session["user"]=username
            return redirect(url_for("welcome"))
        else:
            return Response("Invail crediential ,try again",mimetype="text/plain")