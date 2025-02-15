# routers/prebuilt_resource_instance_routes.py
from flask import Blueprint, request, jsonify
from app.controllers.prebuilt_resource_instance_controller import (
    create_instance,
    get_all_instances,
    get_instance,
    update_instance,
    delete_instance
)

prebuilt_resource_instance_bp = Blueprint('prebuilt_resource_instance_bp', __name__)

# 📌 CREATE PREBUILT RESOURCE INSTANCE (POST)
@prebuilt_resource_instance_bp.route('/', methods=['POST'])
def create_instance_route():
    try:
        data = request.get_json()
        response, status = create_instance(data)
        return jsonify(response), status
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 📌 GET ALL PREBUILT RESOURCE INSTANCES (GET)
@prebuilt_resource_instance_bp.route('/', methods=['GET'])
def get_all_instances_route():
    response, status = get_all_instances()
    return jsonify(response), status

# 📌 GET A SINGLE PREBUILT RESOURCE INSTANCE BY ID (GET)
@prebuilt_resource_instance_bp.route('/<int:instance_id>', methods=['GET'])
def get_instance_route(instance_id):
    response, status = get_instance(instance_id)
    return jsonify(response), status

# 📌 UPDATE PREBUILT RESOURCE INSTANCE (PUT)
@prebuilt_resource_instance_bp.route('/<int:instance_id>', methods=['PUT'])
def update_instance_route(instance_id):
    try:
        data = request.get_json()
        response, status = update_instance(instance_id, data)
        return jsonify(response), status
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 📌 DELETE PREBUILT RESOURCE INSTANCE (DELETE)
@prebuilt_resource_instance_bp.route('/<int:instance_id>', methods=['DELETE'])
def delete_instance_route(instance_id):
    response, status = delete_instance(instance_id)
    return jsonify(response), status
