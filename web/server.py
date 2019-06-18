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


@app.route('/logout',  methods = ["GET"])
def logout():
    session.clear()
    return render_template('index.html')


@app.route('/checkout')
def checkout():
    return render_template('checkout.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/hot')
def hot():
    return render_template('Hot.html')


@app.route('/tooth')
def tooth():
    return render_template('toothbrush.html')


@app.route('/index_log')
def index_log():
    return render_template('index_log.html')


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


@app.route('/static/<content>')
def static_content(content):
    return render_template(content)


@app.route('/users', methods = ['GET'])
def get_users():
    db_session = db.getSession(engine)
    dbResponse = db_session.query(db_models.User)
    data = []
    for user in dbResponse:
        data.append(user)
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype='application/json')


@app.route('/shops', methods = ['GET'])
def get_shops():
    session = db.getSession(engine)
    dbResponse = session.query(db_models.Shop)
    data = []
    for shop in dbResponse:
        data.append(shop)
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype='application/json')


@app.route('/products', methods = ['GET'])
def get_products():
    session = db.getSession(engine)
    dbResponse = session.query(db_models.Products)
    data = []
    for product in dbResponse:
        data.append(product)
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype='application/json')


@app.route('/create_test_users', methods = ['GET'])
def create_test_users():
    db_session = db.getSession(engine)
    user = db_models.User(username="Ale1099", email="ale.20152028@gmail.com", password="1134AA", address="Av. Del Pacifico 20", phone="989989496")
    db_session.add(user)
    db_session.commit()
    return "Test user created!"


@app.route('/create_test_shops', methods = ['GET'])
def create_test_shops():
    db_session = db.getSession(engine)
    shop = db_models.Shop(country="Peru", city="Lima", username= "ale", address="Av. Del Pacifico 180", phone="989989406", comment = "PORFA DEJALO EN LA PUERTA")
    db_session.add(shop)
    db_session.commit()
    return "Test shop created!"


@app.route('/create_test_products', methods = ['GET'])
def create_test_products():
    db_session = db.getSession(engine)
    product = db_models.Product(itemName="Kinesiology Tape",itemDescription ="Vendaje neuromuscular", itemPrice = "35dasd")
    db_session.add(product)
    db_session.commit()
    return "Test product created!"


@app.route('/signup', methods=['POST'])
def signup():
    data = json.loads(request.data)
    user = db_models.User(
        username=data['username'],
        email=data['email'],
        password=data['password'],
        address=data['address'],
        phone=data['phone']
    )
    db_session = db.getSession(engine)
    db_session.add(user)
    db_session.commit()
    return 'Çreated User'


@app.route('/authenticate', methods = ["POST"])
def authenticate():
    message = json.loads(request.data)
    username = message['username']
    password = message['password']
    db_session = db.getSession(engine)
    try:
        user = db_session.query(db_models.User
            ).filter(db_models.User.username == username
            ).filter(db_models.User.password == password
            ).one()
        session['logged_user'] = user.id
        message = {'message': 'Authorized'}
        return Response(message, status=200, mimetype='application/json')
    except Exception:
        message = {'message': 'Unauthorized'}
        return Response(message, status=401, mimetype='application/json')


@app.route('/current', methods = ["GET"])
def current_user():
    db_session = db.getSession(engine)
    user = db_session.query(db_models.User).filter(
        db_models.User.id == session['logged_user']
        ).first()
    return Response(json.dumps(
            user,
            cls=connector.AlchemyEncoder),
            mimetype='application/json'
        )


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=5000, threaded=True, host=('127.0.0.1'))
