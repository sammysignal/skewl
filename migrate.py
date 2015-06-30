#import base64
from tinydb import TinyDB, where
users = TinyDB('db/BackendGlobals.json')

users.insert({"last_school_id": -1, "last_school_id": -1, "last_class_id": -1})