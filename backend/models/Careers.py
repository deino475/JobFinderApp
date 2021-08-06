from flask_sqlalchemy import SQLAlchemy
from models import db

class Careers(db.Model):
	#Unique ID for each career in the database
	id = db.Column(db.String(255), primary_key = True)
	#Name of the career from SOC 
	name = db.Column(db.String(255))
	#Detailed description of career from SOC
	description = db.Column(db.Text)

	def __init__(self, id, name, description):
		'''
		This

		'''
		self.id = id
		self.name = name
		self.description = description