# controllers/prebuilt_resource_instance_controller.py
from app.services.prebuilt_resource_instance_service import (
    create_instance_service,
    get_all_instances_service,
    get_instance_service,
    update_instance_service,
    delete_instance_service,
    create_running_instance
)

def create_instance(data):
    
    try:
        create_instance_service(data)
        create_running_instance(data)
        return {"message": "Prebuilt resource instance created successfully"}, 201
    except Exception as e:
        return {"error": str(e),
                "message":"There was an issue creating the container"}, 500

def get_all_instances():
    return get_all_instances_service()

def get_instance(instance_id):
    return get_instance_service(instance_id)

def update_instance(instance_id, data):
    return update_instance_service(instance_id, data)

def delete_instance(instance_id):
    return delete_instance_service(instance_id)
