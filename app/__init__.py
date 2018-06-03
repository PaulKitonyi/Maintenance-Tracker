from flask import Flask, request, jsonify,abort
from instance.config import app_config
from instance.config import app_config

app = Flask(__name__, instance_relative_config=True)
    
    
requests =[]
users = []       

@app.route('/api/v1/users/requests', methods=["GET"])
def get_all_requests():
    return jsonify({'request':requests})

@app.route('/api/v1/users/requests/<int:id>', methods=["GET"])
def get_single_request(id):
    single_request = [request for request in requests if request['id'] == id]
    return jsonify({'request':single_request})

@app.route('/api/v1/users/requests',methods=["POST"])
def create_request():
    request_add = {'id': len(requests)+1,
            'device type':request.json.get('device type'),
            'request type':request.json.get('request type'),
            'department':request.json.get('department'),
            'description':request.json.get('description')
            }
    requests.append(request_add)
    return jsonify({'Requests': requests}),201

@app.route('/api/v1/users/requests/<int:id>', methods=["PUT"])
def edit_request(id):
    request_edit = [req for req in requests if req["id"] == id]
    if len(request_edit) == 0:
        abort(404)
    request_edit = {
            "device type": request.json.get("device type"),
            "request type": request.json.get('request type'),
            "department": request.json.get("department"),
            "description": request.json.get('description'),
            }
    return jsonify({'requests':request_edit})
            
@app.route('/api/v1/users/requests/<int:id>', methods=["DELETE"])
def delete_request(id):
    delete_request = [req for req in requests if req["id"] == id]
    print(len(delete_request))
    if len(delete_request) == 0:
        abort(404)
    requests.remove(delete_request[0])
    return jsonify({'requests':requests})

# GET all Users
@app.route('/api/v1/users')
def get_users():
    return jsonify({"users": users})

#Register user
@app.route('/api/v1/users', methods=['POST'])
def register_user():
    new_user = {
        "id": len(users)+1,
        "username": request.json.get("username", "username"),
        "email": request.json.get('email'),
        "password": request.json.get("password"),
    }
    # Confirm user entry has data
    for key in new_user:
        if new_user[key] == "":
            return jsonify({"message": "All Fields Required"})

    # Check if passwords match
    if request.json.get("password") != request.json.get("confirm_password"):
        return jsonify({"message": "Your Passwords Don't Match"}), 400
    if len(users) == 0:
        users.append(new_user)
        return jsonify({"message": "Sign Up Successful"}), 201
    for user in users:
        if user["username"] != new_user["username"]:
            users.append(new_user)
            return jsonify({"message": "Sign Up Successful"}), 201
        return jsonify({"message": "User already exists"}), 400
