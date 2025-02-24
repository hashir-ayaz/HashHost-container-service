# controllers/prebuilt_resource_controller.py
from app.services.prebuilt_resource_service import PrebuiltResourceService

class PrebuiltResourceController:
    @staticmethod
    def create_prebuilt_resource(data):
        return PrebuiltResourceService.create_prebuilt_resource_service(data)

    @staticmethod
    def get_all_prebuilt_resources():
        return PrebuiltResourceService.get_all_prebuilt_resources_service()

    @staticmethod
    def get_prebuilt_resource(resource_id):
        return PrebuiltResourceService.get_prebuilt_resource_service(resource_id)

    @staticmethod
    def update_prebuilt_resource(resource_id, data):
        return PrebuiltResourceService.update_prebuilt_resource_service(resource_id, data)

    @staticmethod
    def delete_prebuilt_resource(resource_id):
        return PrebuiltResourceService.delete_prebuilt_resource_service(resource_id)
