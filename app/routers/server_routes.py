from flask import Blueprint, request, jsonify
from app import db
from app.models.server import Server

server_bp = Blueprint('server_bp', __name__)  # No prefix defined here

# ===============================
# 📌 CREATE SERVER (POST)
# ===============================
@server_bp.route('/', methods=['POST'])
def create_server():
    try:
        data = request.get_json()

        if not data or 'name' not in data or 'ip_address' not in data:
            return jsonify({"error": "Missing required fields"}), 400

        new_server = Server(
            name=data['name'],
            ip_address=data['ip_address'],
            status=data.get('status', 'inactive')  # Default to 'inactive' if not provided
        )
        db.session.add(new_server)
        db.session.commit()

        return jsonify({"message": "Server created successfully", "server_id": new_server.id}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ===============================
# 📌 GET ALL SERVERS (GET)
# ===============================
@server_bp.route('/', methods=['GET'])
def get_all_servers():
    servers = Server.query.all()
    server_list = [
        {"id": server.id, "name": server.name, "ip_address": server.ip_address, "status": server.status}
        for server in servers
    ]
    return jsonify(server_list), 200

# ===============================
# 📌 GET A SINGLE SERVER BY ID (GET)
# ===============================
@server_bp.route('/<int:server_id>', methods=['GET'])
def get_server(server_id):
    server = Server.query.get(server_id)
    if not server:
        return jsonify({"error": "Server not found"}), 404

    return jsonify({
        "id": server.id,
        "name": server.name,
        "ip_address": server.ip_address,
        "status": server.status
    }), 200

# ===============================
# 📌 UPDATE SERVER (PUT)
# ===============================
@server_bp.route('/<int:server_id>', methods=['PUT'])
def update_server(server_id):
    server = Server.query.get(server_id)
    if not server:
        return jsonify({"error": "Server not found"}), 404

    try:
        data = request.get_json()

        if 'name' in data:
            server.name = data['name']
        if 'ip_address' in data:
            server.ip_address = data['ip_address']
        if 'status' in data:
            server.status = data['status']

        db.session.commit()
        return jsonify({"message": "Server updated successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ===============================
# 📌 DELETE SERVER (DELETE)
# ===============================
@server_bp.route('/<int:server_id>', methods=['DELETE'])
def delete_server(server_id):
    server = Server.query.get(server_id)
    if not server:
        return jsonify({"error": "Server not found"}), 404

    db.session.delete(server)
    db.session.commit()

    return jsonify({"message": "Server deleted successfully"}), 200
