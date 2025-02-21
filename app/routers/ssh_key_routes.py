from flask import Blueprint, request, jsonify

ssh_key_bp = Blueprint('ssh_key_bp', __name__)

@ssh_key_bp.route('/', methods=['POST'])
def create_ssh_key():
    try:
        data = request.get_json()
        create_ssh_key(data)
        return jsonify({"message": "SSH Key created"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@ssh_key_bp.route('/', methods=['GET'])
def get_all_ssh_keys():
    return jsonify({"message": "Get all SSH Keys"}), 200

@ssh_key_bp.route('/<int:ssh_key_id>', methods=['GET'])
def get_ssh_key(ssh_key_id):
    return jsonify({"message": f"Get SSH Key with ID: {ssh_key_id}"}), 200

@ssh_key_bp.route('/<int:ssh_key_id>', methods=['PUT'])
def update_ssh_key(ssh_key_id):
    return jsonify({"message": f"Update SSH Key with ID: {ssh_key_id}"}), 200

@ssh_key_bp.route('/<int:ssh_key_id>', methods=['DELETE'])
def delete_ssh_key(ssh_key_id):
    return jsonify({"message": f"Delete SSH Key with ID: {ssh_key_id}"}), 200

@ssh_key_bp.route('/int:<server_id',methods=['GET'])
def get_ssh_keys_by_server(server_id):
    return jsonify({"message": f"Get SSH Keys by Server ID: {server_id}"}), 200
