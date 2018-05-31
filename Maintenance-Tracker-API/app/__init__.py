from flask import Flask, request, jsonify
app = Flask(__name__)

requests =[]       

@app.route('/users/requests', methods=["GET"])
def get_all_requests():
    return jsonify({'request':requests})

@app.route('/users/requests/<string:id>', methods=["GET"])
def get_single_request(id):
    single_request = [request for request in requests if request['id'] == id]
    return jsonify({'request':single_request})

@app.route('/users/requests',methods=["POST"])
def create_request():
    request_add = {'id': request.json.get('id'),
            'device type':request.json.get('device type'),
            'request type':request.json.get('request type'),
            'department':request.json.get('department'),
            'description':request.json.get('description')
            }
    requests.append(request_add)
    return jsonify({'Requests': requests})

@app.route('/users/requests/<string:id>', methods=["PUT"])
def edit_request(id):
    request_edit = [req for req in requests if req["id"] == 1]
    request_edit['id'] = request.json.get('id')
    request_edit['device type'] = request.json.get('device type')
    request_edit['request type'] = request.json.get('request type')
    request_edit['department'] = request.json.get('department')
    request_edit['description'] = request.json.get('description')
            
@app.route('/users/requests/<string:id>', methods=["DELETE"])
def delete_request(id):
    delete_request = [req for req in requests if req["id"] == 1]
    requests.remove(delete_request)
    return jsonify({'requests':requests})