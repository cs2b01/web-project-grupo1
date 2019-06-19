from sqlalchemy import Column, Integer, Float, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import connector




class User(connector.Manager.Base):
	__tablename__ = 'users'

	id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
	username = Column(String(20))
	email = Column(String(120))
	password = Column(String(60))
	address = Column(String(200))
	phone = Column(String(20))


class Shop(connector.Manager.Base):
	__tablename__ = 'shops'

	id = Column(Integer,  Sequence('shop_id_seq'), primary_key=True)
	country = Column(String(30))
	city = Column(String(30))
	comment = Column(String(30))
	username = Column(String(30), ForeignKey('users.id'))
	address = Column(String(200), ForeignKey('users.id'))
	phone = Column(String(20), ForeignKey('users.id'))
	username_r = relationship(User, foreign_keys=[username])
	address_r = relationship(User, foreign_keys=[address])
	phone_r = relationship(User, foreign_keys=[phone])


class Product(connector.Manager.Base):
	__tablename__ = 'products'
	id = Column(Integer,  Sequence('product_id_seq'), primary_key=True)
	itemName = Column(String(50))
	itemDescription = Column(String(300))
	itemPrice = Column(String(30))


class Contact(connector.Manager.Base):
	__tablename__ = 'contacts'
	id = Column(Integer, Sequence('contact_id_seq'), primary_key=True)
	name = Column(String(50))
	fullname = Column(String(50))
	email = Column(String(100))
	subject = Column(String(300))
	message = Column(String(300))



class Carito (connector.Manager.Base):
	__tablename__ = 'caritos'
	id = Column(Integer, Sequence('caritos_id_seq'), primary_key=True)
	id_producto = Column(Integer, nullable=False)
	cantidad = Column(Integer, nullable=False)
	username = Column(String)
