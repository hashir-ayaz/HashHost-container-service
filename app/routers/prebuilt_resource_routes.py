# routers/prebuilt_resource_routes.py
from flask import Blueprint, request, jsonify
from app.controllers.prebuilt_resource_controller import (
    create_prebuilt_resource,
    get_all_prebuilt_resources,
    get_prebuilt_resource,
    update_prebuilt_resource,
    delete_prebuilt_resource
)

prebuilt_resource_bp = Blueprint('prebuilt_resource_bp', __name__)

# CREATE PREBUILT RESOURCE (POST)
@prebuilt_resource_bp.route('/', methods=['POST'])
def create_prebuilt_resource_route():
    try:
        data = request.get_json()
        response, status = create_prebuilt_resource(data)
        return jsonify(response), status
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# GET ALL PREBUILT RESOURCES (GET)
@prebuilt_resource_bp.route('/', methods=['GET'])
def get_all_prebuilt_resources_route():
    response, status = get_all_prebuilt_resources()
    return jsonify(response), status

# GET A SINGLE PREBUILT RESOURCE BY ID (GET)
@prebuilt_resource_bp.route('/<int:resource_id>', methods=['GET'])
def get_prebuilt_resource_route(resource_id):
    response, status = get_prebuilt_resource(resource_id)
    return jsonify(response), status

# UPDATE PREBUILT RESOURCE (PUT)
@prebuilt_resource_bp.route('/<int:resource_id>', methods=['PUT'])
def update_prebuilt_resource_route(resource_id):
    try:
        data = request.get_json()
        response, status = update_prebuilt_resource(resource_id, data)
        return jsonify(response), status
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# DELETE PREBUILT RESOURCE (DELETE)
@prebuilt_resource_bp.route('/<int:resource_id>', methods=['DELETE'])
def delete_prebuilt_resource_route(resource_id):
    response, status = delete_prebuilt_resource(resource_id)
    return jsonify(response), status
