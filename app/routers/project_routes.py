# routers/project_routes.py
from flask import Blueprint, request, jsonify
from app.controllers.project_controller import ProjectController

project_bp = Blueprint('project_bp', __name__)  # URL prefix will be set during blueprint registration

# CREATE PROJECT (POST)
@project_bp.route('/', methods=['POST'])
def create_project_route():
    try:
        data = request.get_json()
        response, status = ProjectController.create_project(data)
        return jsonify(response), status
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# GET ALL PROJECTS (GET)
@project_bp.route('/', methods=['GET'])
def get_all_projects_route():
    response, status = ProjectController.get_all_projects()
    return jsonify(response), status

# GET A SINGLE PROJECT BY ID (GET)
@project_bp.route('/<int:project_id>', methods=['GET'])
def get_project_route(project_id):
    response, status = ProjectController.get_project(project_id)
    return jsonify(response), status

# UPDATE PROJECT (PUT)
@project_bp.route('/<int:project_id>', methods=['PUT'])
def update_project_route(project_id):
    try:
        data = request.get_json()
        response, status = ProjectController.update_project(project_id, data)
        return jsonify(response), status
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# DELETE PROJECT (DELETE)
@project_bp.route('/<int:project_id>', methods=['DELETE'])
def delete_project_route(project_id):
    response, status = ProjectController.delete_project(project_id)
    return jsonify(response), status
