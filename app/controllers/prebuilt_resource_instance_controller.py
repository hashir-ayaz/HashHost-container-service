# controllers/prebuilt_resource_instance_controller.py
from app.services.prebuilt_resource_instance_service import PrebuiltResourceInstanceService
from app.models.prebuilt_resource import PrebuiltResource
from app.utils.utils import get_available_ports

class PrebuiltResourceInstanceController:
    
    @staticmethod
    def create_instance(data):
        try:
            # fetch the required ports from data.resource_id , then assign ports using util function assign_ports and pass that to both create_instance_service and create_running_instance
            
            required_ports = PrebuiltResource.query.get(data['resource_id']).required_ports
            available_ports = get_available_ports(required_ports)
            
            PrebuiltResourceInstanceService.create_running_instance(data, available_ports)
            return {"message": "Prebuilt resource instance created successfully"}, 201
        except Exception as e:
            return {"error": str(e),
                    "message":"There was an issue creating the container"}, 500
    
    @staticmethod
    def get_all_instances():
        return PrebuiltResourceInstanceService.get_all_instances_service()
    @staticmethod
    def get_instance(instance_id):
        return PrebuiltResourceInstanceService.get_instance_service(instance_id)
    @staticmethod
    def update_instance(instance_id, data):
        return PrebuiltResourceInstanceService.update_instance_service(instance_id, data)
    @staticmethod
    def delete_instance(instance_id):
        return PrebuiltResourceInstanceService.delete_instance_service(instance_id)
