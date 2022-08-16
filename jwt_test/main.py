from flask import Flask
from flask_jwt import JWT, jwt_required, current_identity

class User():
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return f"User(id={self.id})"

users = [
    User(1, 'user1', 'password'),
    User(2, 'user2', 'abc123')
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username)
    if user and (user.password == password):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'

jwt = JWT(app, authenticate, identity)

@app.route('/protected')
@jwt_required()
def protected():
    return str(current_identity)

app.run(debug = True)