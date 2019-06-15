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


@app.route('/cart')
def cart():
    return render_template('cart.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/checkout')
def checkout():
    return render_template('checkout.html')


@app.route('/contact')
def contacto():
    return render_template('contact.html')


@app.route('/hot')
def hot():
    return render_template('Hot.html')


@app.route('/tooth')
def tooth():
    return render_template('toothbrush.html')


@app.route('/sports')
def sports():
    return render_template('Sports.html')


@app.route('/kine')
def kinesio():
    return render_template('shop-single.html')


@app.route('/thanks')
def thanks():
    return render_template('thankyou.html')


@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/contactinfo', methods = ['POST'])
def info():
    d = json.loads(request.form['values'])
    contacts = entities.User(
        name=d['c_fname'],
        lastname=d['c_lname'],
        email=d['c_email'],
        subject=d['c_subject'],
        message=d['c_message']
    )
    session = db.getSession(engine)
    session.add(contacts)
    session.commit()
    return 'Created User'

@app.route('/static/<content>')
def static_content(content):
    return render_template(content)



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
        return render_template("index2.html"), Response(message, status=200, mimetype='application/json')
    except Exception:
        message = {'message': 'Registrate'}
        return message, render_template("signup.html")




@app.route('/signup', methods = ["POST"])
def create_user():
    data = json.loads(request.data)
    username = data['username']
    email = data['email']
    password = data['password']
    address = data['address']
    phone = data['phone']
    user = db_models.User(
    username = username,
    email = email,
    password = password,
    address = address,
    phone = phone)
    db_session = db.getSession(engine)
    db_session.add(user)
    db_session.commit()
    response = {'user': 'created'}
    return Response(json.dumps(response, cls=connector.AlchemyEncoder), status=200, mimetype='application/json')


@app.route('/authenticate_signup',methods =["POST"])
def authenticate_signup():
    message = json.loads(request.data)
    username = message['username']
    password = message['password']
    email = message ['email'],
    address = message['address'],
    phone = message['phone']
    db_session = db.getSession(engine)

    try:
        user = db_session.query(db_models.User).filter(db_models.User.username == username
                                 ).filter(db_models.User.password == password
                                ).filter(db_models.User.email == email
                                         ).filter(db_models.User.address == address
                                                  ).filter(db_models.User.phone == phone
                                                           ).one()
        session['logged_user'] = user.id
        message = {'message': 'USTED YA ESTA REGISTRADO'}
        return render_template("login.html")

    except Exception:
        message = {'message': 'GRACIAS'}
        return Response(status=200, mimetype='application/json')


if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=5000, threaded=True, host=('127.0.0.1'))
