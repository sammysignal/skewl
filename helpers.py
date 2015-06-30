from flask import Flask
from tinydb import TinyDB, where
import base64

users = TinyDB('db/users.json')
schools = TinyDB('db/schools.json')
backend_globals = TinyDB('db/BackendGlobals.json')

def base36encode(number, alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
	"""Converts an integer to a base36 string."""
	if not isinstance(number, (int, long)):
		raise TypeError('number must be an integer')

	base36 = ''
	sign = ''

	if number < 0:
		sign = '-'
		number = -number

	if 0 <= number < len(alphabet):
		return sign + alphabet[number]
	while number != 0:
		number, i = divmod(number, len(alphabet))
		base36 = alphabet[i] + base36

	return sign + base36

def base36decode(number):
	return int(number, 36)

def get_hash_from_id(_id):
	h = base36encode(_id)
	for i in range(6 - len(h)):
		h = "0" + h
	return h

def get_id_from_hash(_hash):
	return base36decode(_hash)

# returns user object from db, else return 0.
def get_user_by_username(username):
	usr = users.search(where('username') == username)
	if len(usr) > 1:
		raise Exception("Found more than one user with username '" + username + "'")
	if usr:
		return {'username': username, 'password': usr[0]["password"], 'id': usr[0]["id"]}
	# No such user found, return 0
	return 0

# Saves new user to database. returns 0 on 'user with that username already exists'
def save_new_user(username, password):
	if (get_user_by_username(username)):
		return False
	users.insert({'username': username, 'password': password})
	return True

def get_school_by_name(name):
	school = schools.search(where('name') == name)
	if len(usr) > 1:
		raise Exception("Found more than one user with username '" + username + "'")
	if usr:
		return {'username': username, 'password': usr[0]["password"]}
	# No such user found, return 0
	return 0


def get_last_user_id():
	return backend_globals.all()[0]["last_user_id"]

def get_last_school_id():
	return backend_globals.all()[0]["last_school_id"]

def get_last_class_id():
	return backend_globals.all()[0]["last_school_id"]


# name ~ "string", location ~ {"state", "City"}
def register_new_school(school_name, location):
	pass
def get_all_schools():
	pass
def get_school_by_id(school_id):
	pass
def get_school_id_by_name(school_name):
	pass


def register_new_class(class_name):
	pass
def get_all_classes_for_school(school_id):
	pass
def get_class_by_name(class_name, school_id=None):
	pass



def test_base36_encoding():
	assert(base36encode(35) == "Z")
	assert(base36encode(36) == "10")
	for i in range(10):
		assert(base36encode(i) == str(i))
	assert(base36decode("Z") == 35)
	assert(base36decode("10") == 36)
	assert(base36decode("9") == 9)
	assert(base36decode("0000009") == 9)
	return

