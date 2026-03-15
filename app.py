from flask import Flask,request,redirect,url_for,session,Response

app=Flask(__name__)
app.secret_key="supersecret"

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
    return"""
        <h2>LOGIN</h2>
        <form method="POST">
        username:<input type="text" name="username"><br>
        password:<input type="password" name="password"><br>
        <input type="submit" value="login">
        </form>
          
    """

#welcome page
@app.route("/welcome")
def welcome():
    if "user" in session:
        return'''
    <h2>Welcome ,{session["user"]}!!</h2>
    <a href={url_for('logout')}>logout</a>
    '''
    return redirect(url_for("login"))

#logout
@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))
        
    
    