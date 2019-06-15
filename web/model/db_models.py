from sqlalchemy import Column, Integer, Float, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import connector




class User(connector.Manager.Base):
	__tablename__ = 'User'

	id = Column(Integer, primary_key=True)
	username = Column(String(20), unique=True, nullable=False)
	email = Column(String(120), unique=True, nullable=False)
	password = Column(String(60), nullable=False)
	address = Column(String(200))
	phone = Column(String(20))


class Shop(connector.Manager.Base):
	__tablename__ = 'Shop'

	id = Column(Integer, primary_key=True)
	country = Column(String(30))
	city= Column(String(30))
	name = Column(String(30), ForeignKey(User.id))
	fullname = Column(String(30), ForeignKey(User.id))
	address = Column(String(200), ForeignKey(User.id))
	phone = Column(String(20), ForeignKey(User.id))
	comment = Column(String(30))
	name_r = relationship(User, foreign_keys=[name])
	fullname_r = relationship(User, foreign_keys=[fullname])
	address_r = relationship(User, foreign_keys=[address])
	phone_r = relationship(User, foreign_keys=[phone])


class Products(connector.Manager.Base):
	__tablename__ = 'Products'
	id = Column(Integer, primary_key=True)
	itemName = Column(String(30), unique=True, nullable=False)
	itemMainDescription = Column(String(30))
	itemPointsDescription = Column(String(200))
	itemImage = Column(String(30), nullable=False)
	itemPrice = Column(Float(10,2), nullable=False)

class Carito (connector.Manager.Base):
	__tablename__ = 'Carito'
	id = Column(Integer, primary_key=True)
	producto_id = Column(Integer, nullable=False)
	cantidad = Column(Integer, nullable=False)
	user_id = Column(Integer, nullable=False)

