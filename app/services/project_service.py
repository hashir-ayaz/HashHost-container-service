# services/project_service.py
from app import db
from app.models.project import Project
from app.models.server import Server

class ProjectService:

    @staticmethod
    def create_project_service(data):
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

    @staticmethod
    def get_all_projects_service():
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

    @staticmethod
    def get_project_service(project_id):
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

    @staticmethod
    def update_project_service(project_id, data):
        project = Project.query.get(project_id)
        if not project:
            return {"error": "Project not found"}, 404

        if 'name' in data:
            project.name = data['name']
        if 'description' in data:
            project.description = data['description']
        if 'server_id' in data:
            # Validate new server exists
            server = Server.query.get(data['server_id'])
            if not server:
                return {"error": "Server not found"}, 404
            project.server_id = data['server_id']

        db.session.commit()
        return {"message": "Project updated successfully"}, 200

    @staticmethod
    def delete_project_service(project_id):
        project = Project.query.get(project_id)
        if not project:
            return {"error": "Project not found"}, 404

        db.session.delete(project)
        db.session.commit()
        return {"message": "Project deleted successfully"}, 200
