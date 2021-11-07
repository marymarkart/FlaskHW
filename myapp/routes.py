from myapp import myapp_obj
from myapp.forms import LoginForm
from flask import render_template, flash, redirect


@myapp_obj.route("/", methods=['GET','POST'])
def home():
	title = "Top Cities"
	name = "Mary"
	top_cities = [{'city_name': 'Rio', 'city_rank': 10, 'visted': False}]
	form = LoginForm()
	if form.validate_on_submit():
		flash(f'{form.city_name.data} was added!')
		return redirect("/")
	return render_template('home.html', title=title, name=name, top_cities=top_cities, form=form)
