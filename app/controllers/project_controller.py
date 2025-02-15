# controllers/project_controller.py
from app.services.project_service import (
    create_project_service,
    get_all_projects_service,
    get_project_service,
    update_project_service,
    delete_project_service
)

def create_project(data):
    return create_project_service(data)

def get_all_projects():
    return get_all_projects_service()

def get_project(project_id):
    return get_project_service(project_id)

def update_project(project_id, data):
    return update_project_service(project_id, data)

def delete_project(project_id):
    return delete_project_service(project_id)
