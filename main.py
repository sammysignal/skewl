from flask import Flask, request, session, redirect, url_for, render_template
from user import User
from helpers import *
from tinydb import TinyDB, where
import base64
app = Flask(__name__)
users = TinyDB('db/users.json')

app.secret_key = 's\xdbF\x1eG.\xd3m\x8aA\x1a\x8d\xd2\xa1jk\x05\xb7\xf4\x10R\xce\xe4\xdc'

@app.route("/", methods=['GET'])
def home():
	if 'username' in session:
		# logged in!
		return render_template('home.html', username=session['username'])
	else:
		return render_template('home.html')

@app.route("/login/", methods=['GET', 'POST'])
def login():
	if 'username' in session:
		redirect(url_for('home'))

	if request.method == 'GET':
		return render_template('login.html', error=0)

	if request.method == 'POST':
		if (not 'username' in request.form) or (not 'password' in request.form):
			# login failed - incomplete form
			return render_template('login.html', error=1)
		usr = get_user_by_username(request.form['username'])
		if usr:
			if usr.password == base64.b64encode(request.form['password']):
				session['username'] = request.form['username']
				redirect(url_for('home'))
			else:
				# login failed - bad credentials
				return render_template('login.html', error=2)
		else:
			# login failed - username does not exist
			return render_template('login.html', error=2)
	else:
		abort(405)

	return redirect(url_for('home'))

@app.route("/signup/", methods=['GET', 'POST'])
def signup():
	if 'username' in session:
		redirect(url_for('home'))

	if request.method == 'GET':
		return render_template('signup.html', error=0)

	if request.method == 'POST':
		print("posting new user...")
		print(request.form)
		if (not request.form['username']) or \
		   (not request.form['password']) or \
		   (not request.form['passwordconfirm']):
			print("0")
			# login failed - incomplete form
			return render_template('signup.html', error=1)
		if request.form['password'] != request.form['passwordconfirm']:
			print("1")
			# login failed - passwords do not match
			return render_template('signup.html', error=2)
		print("about to save new user...")
		usr = save_new_user(request.form['username'], base64.b64encode(request.form['password']))
		if usr:
			print("saved successfully")
			session['username'] = request.form['username']
			return redirect(url_for('home'))
		else:
			# login failed - that username is already taken
			return render_template('signup.html', error=3)
	else:
		abort(405)
	return redirect(url_for('home'))

@app.route("/logout/", methods=['POST'])
def logout():
	if request.method == 'POST':
		if 'username' in session:
			session.pop('username', None)
	return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug = True)


