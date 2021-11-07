from myapp import db
from datetime import datetime

class City(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	city_name = db.Column(db.String(64), unique=True, index=True)
	city_rank = db.Column(db.Integer, index=True)
	is_visted = db.Column(db.Boolean)

	def __init__(self, city_name, city_rank, is_visited):
		self.city_name =city_name
		self.city_rank = city_rank
		self.is_visited = is_visited

	def __repr__(self):
		return '<City {}>'.format(self.city_name)
		
