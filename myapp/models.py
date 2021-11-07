class City:(db.Model):
	city_name = db.Column(db.String(64), primary_key=True)
	city_rank = db.Column(db.Integer, index=True)
	is_visted = db.Column(db.Boolean)

	def __repr__(self):
		return '<City {}>'.format(self.city_name)
