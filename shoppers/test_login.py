from flask import Flask, render_template, request, redirect, flash
import json
from models import db_models

app = Flask(__name__)
app.secret_key = 'some_secret_key'


@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        flash("Welcome {}! Have a nice day!".format(request.form["username"]))
        lst = [["Username", request.form["username"]], ["Date of birth", request.form["dob"]],["Email", request.form["email"]], ["Gender", request.form["gender"]]]
        return render_template("index.html", lst=lst)
    else:
        return render_template("login.html")

@app.route('/users', methods = ['POST'])
def create_user():
    c =  json.loads(request.form['values'])
    user = db_models.User(
        username=c['username'],
        email=c['email'],
        password=c['password'],
        adress=c['adress'],
        phone =c['phone']
    )
    session = db.getSession(engine)
    session.add(user)
    session.commit()
    return 'Created User'

if __name__ == "__main__":
    app.debug = True
    app.run()
