# controllers/prebuilt_resource_controller.py
from app.services.prebuilt_resource_service import (
    create_prebuilt_resource_service,
    get_all_prebuilt_resources_service,
    get_prebuilt_resource_service,
    update_prebuilt_resource_service,
    delete_prebuilt_resource_service
)

def create_prebuilt_resource(data):
    return create_prebuilt_resource_service(data)

def get_all_prebuilt_resources():
    return get_all_prebuilt_resources_service()

def get_prebuilt_resource(resource_id):
    return get_prebuilt_resource_service(resource_id)

def update_prebuilt_resource(resource_id, data):
    return update_prebuilt_resource_service(resource_id, data)

def delete_prebuilt_resource(resource_id):
    return delete_prebuilt_resource_service(resource_id)
