from flask import Flask,render_template, request, session, Response, redirect
from database import connector
from model import db_models
import json


db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/static/<content>')
def static_content(content):
    return render_template


@app.route('/users', methods = ['GET'])
def get_users():
    session = db.getSession(engine)
    dbResponse = session.query(db_models.User)
    data = []
    for user in dbResponse:
        data.append(user)
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype='application/json')


@app.route("/users", methods=["GET", "POST"])
def signup():
    c =  json.loads(request.form['values'])
    new_user = db_models.User(
        username=c['username'],
        email=c['email'],
        password=c['password'],
        adress=c['adress'],
        phone =c['phone']
    )
    session = db.getSession(engine)
    session.add(new_user)
    session.commit()
    return 'Created User'


@app.route('/authenticatelogin',methods =["POST"])
def authenticatelogin():
    message = json.loads(request.data)
    username = message['username']
    password = message['password']
    db_session = db.getSession(engine)

    try:
        user = db_session.query(db_models.User
                               ).filter(db_models.User.username == username
                                 ).filter(db_models.User.password == password
                                ).one()
        message = {'message': 'Authorized'}
        return Response(message, status=200, mimetype='application/json')

    except Exception:
        message = {'message': 'Unauthorized'}
        return Response(message, status=401, mimetype='application/json')


@app.route('/authenticatesignup',methods =["POST"])
def authenticatesignup():
    message = json.loads(request.data)
    username = message['username']
    password = message['password']
    email = ['email'],
    adress = ['adress'],
    phone = ['phone']
    db_session = db.getSession(engine)

    try:
        user = db_session.query(db_models.User).filter(db_models.User.username == username
                                 ).filter(db_models.User.password == password
                                ).filter(db_models.User.email == email
                                         ).filter(db_models.User.adress == adress
                                                  ).filter(db_models.User.phone== phone
                                                           ).one()
        message = {'message': 'Authorized'}
        return Response(message, status=200, mimetype='application/json')

    except Exception:
        message = {'message': 'Unauthorized'}
        return Response(message, status=401, mimetype='application/json')





if __name__ == "__main__":
    app.debug = True
    app.run()
