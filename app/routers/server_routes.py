# routers/server_routes.py
from flask import Blueprint, request, jsonify
from app.controllers.server_controller import ServerController

server_bp = Blueprint('server_bp', __name__)  # No URL prefix defined here; set it when registering the blueprint

# CREATE SERVER (POST)
@server_bp.route('/', methods=['POST'])
def create_server_route():
    try:
        data = request.get_json()
        response, status = ServerController.create_server(data)
        return jsonify(response), status
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# GET ALL SERVERS (GET)
@server_bp.route('/', methods=['GET'])
def get_all_servers_route():
    response, status = ServerController.get_all_servers()
    return jsonify(response), status

# GET A SINGLE SERVER BY ID (GET)
@server_bp.route('/<int:server_id>', methods=['GET'])
def get_server_route(server_id):
    response, status = ServerController.get_server(server_id)
    return jsonify(response), status

# UPDATE SERVER (PUT)
@server_bp.route('/<int:server_id>', methods=['PUT'])
def update_server_route(server_id):
    try:
        data = request.get_json()
        response, status = ServerController.update_server(server_id, data)
        return jsonify(response), status
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# DELETE SERVER (DELETE)
@server_bp.route('/<int:server_id>', methods=['DELETE'])
def delete_server_route(server_id):
    response, status = ServerController.delete_server(server_id)
    return jsonify(response), status
