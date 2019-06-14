from flask import Flask,render_template, request, session, Response, redirect
from database import connector


db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

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


if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=5000, threaded=True, host=('127.0.0.1'))
