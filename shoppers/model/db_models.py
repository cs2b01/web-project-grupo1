from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import connector


class User(connector.Manager.Base):
	__tablename__ = 'User'

	id = Column(Integer, primary_key=True)
	username = Column(String(20), unique=True, nullable=False)
	email = Column(String(120), unique=True, nullable=False)
	password = Column(String(60), nullable=False)
	adress = Column(String(200))
	phone = Column(String(20))

	def __repr__(self):
		return f"User('{self.name}', '{self.mail}')"


class Item(connector.Manager.Base):
	__tablename__ = 'Item'

	id = Column(Integer, primary_key=True)
	itemName = Column(String(30), unique=True, nullable=False)
	itemMainDescription = Column(String(30))
	itemPointsDescription = Column(String(200))
	itemImage = Column(String(30), nullable=False)
	itemPrice = Column(Integer, nullable=False)

	def __repr__(self):
		return f"Item('{self.itemName}')"

