# controllers/project_controller.py
from app.services.project_service import ProjectService

class ProjectController:

    @staticmethod
    def create_project(data):
        return ProjectService.create_project_service(data)

    @staticmethod
    def get_all_projects():
        return ProjectService.get_all_projects_service()

    @staticmethod
    def get_project(project_id):
        return ProjectService.get_project_service(project_id)

    @staticmethod
    def update_project(project_id, data):
        return ProjectService.update_project_service(project_id, data)

    @staticmethod
    def delete_project(project_id):
        return ProjectService.delete_project_service(project_id)
