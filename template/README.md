# Fluffy Knives - online shop app
Online shop app created with Python, Flask, SQLAlchemy, Bootstrap.

Link to deployed app: http://fluffyknives.herokuapp.com/

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Features](#features)
* [Setup](#setup)
* [Inspiration](#inspiration)
* [Contact](#contact)

## General info
This app was created for educational purposes on my own.

All of the content comes from our knives crafting work and we wanted to present it as well.

## Technologies
* Python 3.6.3
* Flask 1.0.2
* SQLAlchemy 1.2.9
* Bootstrap 4.1.1

## Features
* Shop presentation with info and avaliable products generated from the shop database
* Different templates for not logged user, logged user and admin

User account:
* User account registration, login and logout
* User account data editing, adding profile photo
* Making orders
* User orders page with order status info

Admin account:
* Adding new products to the shop database, with product description and photo
* Deleting products from the database
* Orders page with all users orders info
* Ability to change order's status

Admin login credentials:

login: admin@admin.admin

password: admin

## Setup
To run the app:
1. Install Python 3.6.3
2. Install virtual environment:
		python -m venv [path]
3. Run virtual environment:
		[path]\Scripts\activate.bat
4. Install Flask micro-framework:
		pip install Flask
5. Install WTForms:
		pip install flask-wtf
6. Install Flask-SQLAlchemy:
		pip install flask-sqlalchemy
7. Install Flask-Bcrypt:
		pip install flask-bcrypt
8. Install Flask-Login:
		pip install flask-login
5. Install Pillow:
		pip install Pillow
6. Run the app from main app folder:
		python run.py

Requirements:

bcrypt==3.1.4
cffi==1.11.5
click==6.7
Flask==1.0.2
Flask-Bcrypt==0.7.1
Flask-Login==0.4.1
Flask-SQLAlchemy==2.3.2
Flask-WTF==0.14.2
gunicorn==19.7.1
itsdangerous==0.24
Jinja2==2.10
MarkupSafe==1.0
Pillow==5.2.0
pycparser==2.18
six==1.11.0
SQLAlchemy==1.2.9
Werkzeug==0.14.1
WTForms==2.2.1

## Inspiration
All of the content comes from our knives crafting work. 

All of the photos and the video are my job.

The app was partly based on Flask tutorial: https://www.youtube.com/watch?v=MwZwr5Tvyxo

JS for navbar was taken from https://startbootstrap.com/ , JS for smooth scrolling was taken from https://css-tricks.com/snippets/jquery/smooth-scrolling/

All other sources of knowledge are:
* Python, Bootstrap, Flask framework and libraries documentations
* "Python Level Up" course organised by Daftcode.
* https://stackoverflow.com/

## Contact
App created by Urszula Poliszuk.

Feel free to contact me: urszulapoliszuk@gmail.com
