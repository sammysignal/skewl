from flask import Flask, request, session, redirect, url_for
from user import User
from helpers import *
from tinydb import TinyDB, where
import base64
app = Flask(__name__)
users = TinyDB('db/users.json')

@app.route("/", methods=['GET'])
def home():
	if session['username']:
		# logged in! TODO TODO
	else:

@app.route("/login/", methods=['GET', 'POST'])
def login():
	if 'username' in session:
		redirect(url_for('home'))

	if request.method == 'GET':
		return render_template('login.html', error=0)

	if request.method == 'POST':
		if (not 'username' in request.form)) or (not 'password' in request.form):
			# login failed - incomplete form
			return render_template('login.html', error=1)
		usr = get_user_by_username(request.form['username'])
		if usr:
			if usr.password == base64.b64encode(request.form['password']):
				session['username'] == request.form['username']
				redirect(url_for('home'))
			else:
				# login failed - bad credentials
				return render_template('login.html', error=2)
		else:
			# login failed - username does not exist
			return render_template('login.html', error=2)
	else:
		abort(405)
    return request

@app.route("/signup/", methods=['GET', 'POST'])
def signup():
	if 'username' in session:
		redirect(url_for('home'))

	if request.method == 'GET':
		return render_template('signup.html', error=0)

	if request.method == 'POST':
		if (not 'username' in request.form)) or 
		   (not 'password' in request.form) or
		   (not 'password_confirm' in request.form):
			return render_template('signup.html', error=1)

		usr = save_new_user(request.form['username'], request.form['password'])
		if usr:
			session['username'] == request.form['username']
			redirect(url_for('home'))
		else:
			return render_template('login.html', error=2)
	else:
		abort(405)
    return request

@app.route("/logout/", methods=['POST'])
def logout():
	if request.method == 'POST':
		if 'username' in request.form:
	    	session.pop('username', None)
	    	return redirect(url_for('home'))
	return redirect('home')


if __name__ == "__main__":
    app.run(debug = True)


