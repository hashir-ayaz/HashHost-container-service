from flask import Blueprint, request, jsonify
from app import db
from app.models.project import Project
from app.models.server import Server

project_bp = Blueprint('project_bp', __name__)  # No prefix, define in init.py or run.py

# ===============================
# 📌 CREATE PROJECT (POST)
# ===============================
@project_bp.route('/', methods=['POST'])
def create_project():
    try:
        data = request.get_json()

        if not data or 'name' not in data or 'server_id' not in data:
            return jsonify({"error": "Missing required fields"}), 400

        # Ensure the server exists before assigning a project
        server = Server.query.get(data['server_id'])
        if not server:
            return jsonify({"error": "Server not found"}), 404

        new_project = Project(
            name=data['name'],
            description=data.get('description', ""),  # Default to empty string if not provided
            server_id=data['server_id']
        )
        db.session.add(new_project)
        db.session.commit()

        return jsonify({"message": "Project created successfully", "project_id": new_project.id}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ===============================
# 📌 GET ALL PROJECTS (GET)
# ===============================
@project_bp.route('/', methods=['GET'])
def get_all_projects():
    projects = Project.query.all()
    project_list = [
        {
            "id": project.id,
            "name": project.name,
            "description": project.description,
            "server_id": project.server_id,
            "created_at": project.created_at,
            "updated_at": project.updated_at
        }
        for project in projects
    ]
    return jsonify(project_list), 200

# ===============================
# 📌 GET A SINGLE PROJECT BY ID (GET)
# ===============================
@project_bp.route('/<int:project_id>', methods=['GET'])
def get_project(project_id):
    project = Project.query.get(project_id)
    if not project:
        return jsonify({"error": "Project not found"}), 404

    return jsonify({
        "id": project.id,
        "name": project.name,
        "description": project.description,
        "server_id": project.server_id,
        "created_at": project.created_at,
        "updated_at": project.updated_at
    }), 200

# ===============================
# 📌 UPDATE PROJECT (PUT)
# ===============================
@project_bp.route('/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    project = Project.query.get(project_id)
    if not project:
        return jsonify({"error": "Project not found"}), 404

    try:
        data = request.get_json()

        if 'name' in data:
            project.name = data['name']
        if 'description' in data:
            project.description = data['description']
        if 'server_id' in data:
            server = Server.query.get(data['server_id'])
            if not server:
                return jsonify({"error": "Server not found"}), 404
            project.server_id = data['server_id']

        db.session.commit()
        return jsonify({"message": "Project updated successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ===============================
# 📌 DELETE PROJECT (DELETE)
# ===============================
@project_bp.route('/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    project = Project.query.get(project_id)
    if not project:
        return jsonify({"error": "Project not found"}), 404

    db.session.delete(project)
    db.session.commit()

    return jsonify({"message": "Project deleted successfully"}), 200
