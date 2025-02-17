# controllers/prebuilt_resource_instance_controller.py
from app.services.prebuilt_resource_instance_service import (
    create_instance_service,
    get_all_instances_service,
    get_instance_service,
    update_instance_service,
    delete_instance_service,
    create_running_instance
)
from app.models.prebuilt_resource import PrebuiltResource
from app.utils.utils import get_available_ports

def create_instance(data):
    
    try:
        # fetch the required ports from data.resource_id , then assign ports using util function assign_ports and pass that to both create_instance_service and create_running_instance
        
        required_ports = PrebuiltResource.query.get(data['resource_id']).required_ports
        available_ports = get_available_ports(required_ports)
        
        create_running_instance(data, available_ports)
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
