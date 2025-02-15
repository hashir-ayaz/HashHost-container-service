# controllers/project_controller.py
from app import db
from app.models.project import Project
from app.models.server import Server

def create_project(data):
    # Validate required fields
    if not data or 'name' not in data or 'server_id' not in data:
        return {"error": "Missing required fields"}, 400

    # Ensure the server exists before assigning a project
    server = Server.query.get(data['server_id'])
    if not server:
        return {"error": "Server not found"}, 404

    new_project = Project(
        name=data['name'],
        description=data.get('description', ""),  # Default to empty string if not provided
        server_id=data['server_id']
    )
    db.session.add(new_project)
    db.session.commit()

    return {"message": "Project created successfully", "project_id": new_project.id}, 201

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
    return project_list, 200

def get_project(project_id):
    project = Project.query.get(project_id)
    if not project:
        return {"error": "Project not found"}, 404

    return {
        "id": project.id,
        "name": project.name,
        "description": project.description,
        "server_id": project.server_id,
        "created_at": project.created_at,
        "updated_at": project.updated_at
    }, 200

def update_project(project_id, data):
    project = Project.query.get(project_id)
    if not project:
        return {"error": "Project not found"}, 404

    if 'name' in data:
        project.name = data['name']
    if 'description' in data:
        project.description = data['description']
    if 'server_id' in data:
        server = Server.query.get(data['server_id'])
        if not server:
            return {"error": "Server not found"}, 404
        project.server_id = data['server_id']

    db.session.commit()
    return {"message": "Project updated successfully"}, 200

def delete_project(project_id):
    project = Project.query.get(project_id)
    if not project:
        return {"error": "Project not found"}, 404

    db.session.delete(project)
    db.session.commit()
    return {"message": "Project deleted successfully"}, 200
