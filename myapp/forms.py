from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	city_name =  StringField('City Name', validators=[DataRequired()])
	city_rank = IntegerField('City Rank')	
	is_visited = BooleanField('Visited')
	submit = SubmitField("Submit")
