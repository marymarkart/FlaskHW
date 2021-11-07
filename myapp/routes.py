from myapp import myapp_obj
from myapp.forms import LoginForm
from flask import render_template, request, flash, redirect
from myapp.models import City
from myapp import db

@myapp_obj.route("/", methods=['GET','POST'])
def home():
	title = "Top Cities"
	name = "Mary"
	top_cities = City.query.all()
	form = LoginForm()
	if form.validate_on_submit():
		flash(f'{form.city_name.data} was added!')
		city_name = form.city_name.data
		city_rank = form.city_rank.data
		is_visited = form.is_visited.data
		city = City(city_name, city_rank, is_visited)
		db.session.add(city)
		db.session.commit()
		return redirect("/")
	return render_template('home.html', title=title, name=name, top_cities=top_cities, form=form)
