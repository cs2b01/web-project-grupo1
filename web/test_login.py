from flask import Flask,render_template, request, session, Response, redirect
from database import connector
from model import db_models
import json

from models import db_models


db = connector.Manager()
engine = db.createEngine()


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/static/<content>')
def static_content(content):
    return render_template(content)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/users', methods = ['GET'])
def get_users():
    session = db.getSession(engine)
    dbResponse = session.query(db_models.User)
    data = []
    for user in dbResponse:
        data.append(user)
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype='application/json')


@app.route('/login', methods=['POST'])
def login_post():
    message = json.loads(request.data)
    username = message['username']
    password = message['password']
    db_session = db.getSession(engine)

    try:
        user = db_session.query(db_models.User
                                ).filter(db_models.User.username == username
                                         ).filter(db_models.User.password == password
                                                  ).one()
        message = {'message': 'HOLA', username: username}
        return render_template("index.html"), Response(message, status=200, mimetype='application/json')
    except Exception:
        message = {'message': 'Registrate'}
        return message, render_template("signup.html")


@app.route("/signup", methods=["POST"])
def signup_post():
    c = json.loads(request.form['values'])
    user = db_models.User(
        username=c['username'],
        email=c['email'],
        password=c['password'],
        adress=c['address'],
        phone=c['phone']
    )
    session = db.getSession(engine)
    session.add(user)
    session.commit()
    return render_template("index.html")


@app.route('/authenticate_signup',methods =["POST"])
def authenticate_signup():
    message = json.loads(request.data)
    username = message['username']
    password = message['password']
    email = ['email'],
    address = ['address'],
    phone = ['phone']
    db_session = db.getSession(engine)

    try:
        user = db_session.query(db_models.User).filter(db_models.User.username == username
                                 ).filter(db_models.User.password == password
                                ).filter(db_models.User.email == email
                                         ).filter(db_models.User.address == address
                                                  ).filter(db_models.User.phone== phone
                                                           ).one()
        message = {'message': 'Authorized'}
        return Response(message, status=200, mimetype='application/json')

    except Exception:
        message = {'message': 'Unauthorized'}
        return Response(message, status=401, mimetype='application/json')


@app.route('/contact_me', methods=['POST'])
def contact_me():
    info = json.loads(request.data)
    username = message['username']
    password = message['password']
    db_session = db.getSession(engine)
    user = db_session.query(db_models.User).filter(db_models.User.username == username
    ).filter(db_models.User.password == password).one()

    return render_template("/static/thankyou.html"), Response(message, status=200, mimetype='application/json')




if __name__ == "__main__":
    app.debug = True
    app.run()
