from flask import jsonify, request
from app import app, db
from app.models import User

@app.route('/')
def home():
    return jsonify({'message': "Welcome to the Flask API!"}) # return a JSON response
@app.route('/users', methods=['GET', 'POST'])
def manage_users():
        if request.method == 'GET':
            users = User.query.all()
            users = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
            return jsonify(users)
        elif request.method == 'POST':
            data = request.get_json()
            user = User(username=data['username'], email=data['email'])
            db.session.add(user)
            db.session.commit()
            return jsonify({'message': 'User created!'})