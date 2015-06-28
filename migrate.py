#import base64
from tinydb import TinyDB, where
users = TinyDB('db/users.json')

username = 'smehr'
print(users.search(where('username') == username))