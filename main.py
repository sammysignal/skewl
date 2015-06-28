from user import User
from flask import Flask
from tinydb import TinyDB, where
app = Flask(__name__)
users = TinyDB('db/users.json')

@app.route("/")
def home():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug = True)


