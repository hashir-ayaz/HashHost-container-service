# routers/prebuilt_resource_routes.py
from flask import Blueprint, request, jsonify
from app.controllers.prebuilt_resource_controller import PrebuiltResourceController

prebuilt_resource_bp = Blueprint('prebuilt_resource_bp', __name__)

# CREATE PREBUILT RESOURCE (POST)
@prebuilt_resource_bp.route('/', methods=['POST'])
def create_prebuilt_resource_route():
    try:
        data = request.get_json()
        response, status = PrebuiltResourceController.create_prebuilt_resource(data)
        return jsonify(response), status
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# GET ALL PREBUILT RESOURCES (GET)
@prebuilt_resource_bp.route('/', methods=['GET'])
def get_all_prebuilt_resources_route():
    response, status = PrebuiltResourceController.get_all_prebuilt_resources()
    return jsonify(response), status

# GET A SINGLE PREBUILT RESOURCE BY ID (GET)
@prebuilt_resource_bp.route('/<int:resource_id>', methods=['GET'])
def get_prebuilt_resource_route(resource_id):
    response, status = PrebuiltResourceController.get_prebuilt_resource(resource_id)
    return jsonify(response), status

# UPDATE PREBUILT RESOURCE (PUT)
@prebuilt_resource_bp.route('/<int:resource_id>', methods=['PUT'])
def update_prebuilt_resource_route(resource_id):
    try:
        data = request.get_json()
        response, status = PrebuiltResourceController.update_prebuilt_resource(resource_id, data)
        return jsonify(response), status
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# DELETE PREBUILT RESOURCE (DELETE)
@prebuilt_resource_bp.route('/<int:resource_id>', methods=['DELETE'])
def delete_prebuilt_resource_route(resource_id):
    response, status = PrebuiltResourceController.delete_prebuilt_resource(resource_id)
    return jsonify(response), status
