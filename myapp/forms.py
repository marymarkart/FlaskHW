from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	city_name =  StringField('City Name', validators=[DataRequired()])
	city_rank = IntegerField('City Rank', validators=[DataRequired()])	
	is_visited = BooleanField('Visited', default=False)
	submit = SubmitField("Submit")
