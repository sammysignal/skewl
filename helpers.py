from user import User
from flask import Flask
from tinydb import TinyDB, where
import base64
app = Flask(__name__)
users = TinyDB('db/users.json')

# returns user object from db, else return 0.
def get_user_by_username(username):
	usr = users.search(where('username') == username)
	if len(usr) > 1:
		raise Exception("Found more than one user with username '" + username + "'")
	if usr:
		return User(username, usr[0]["password"])
	# No such user found, return 0
	return 0

# Saves new user to database. returns 0 on 'user with that username already exists'
def save_new_user(username, password):
	if (get_user_by_username(username)):
		return False
	users.insert({'username': username, 'password': password})
	return True