# services/prebuilt_resource_service.py
from app import db
from app.models.prebuilt_resource import PrebuiltResource

class PrebuiltResourceService:
    @staticmethod
    def create_prebuilt_resource_service(data):
        if not data or 'name' not in data or 'image' not in data or 'required_ports' not in data or not data['required_ports'] or 'volume_path' not in data:
            return {"error": "Missing required fields"}, 400



        # saving to db 
        new_resource = PrebuiltResource(
            name=data['name'],
            description=data.get('description', ""),
            image=data['image'],
            default_config=data.get('default_config', {}),
            required_ports=data['required_ports'],
            volume_path=data.get('volume_path')
        )
        db.session.add(new_resource)
        db.session.commit()
        return {"message": "Prebuilt resource created successfully", "resource_id": new_resource.id}, 201

    @staticmethod
    def get_all_prebuilt_resources_service():
        resources = PrebuiltResource.query.all()
        resource_list = [
            {
                "id": resource.id,
                "name": resource.name,
                "description": resource.description,
                "image": resource.image,
                "default_config": resource.default_config,
                "required_ports": resource.required_ports,
                "created_at": resource.created_at,
                "updated_at": resource.updated_at,
                "volume_path": resource.volume_path
            }
            for resource in resources
        ]
        return resource_list, 200

    @staticmethod
    def get_prebuilt_resource_service(resource_id):
        resource = PrebuiltResource.query.get(resource_id)
        if not resource:
            return {"error": "Prebuilt resource not found"}, 404

        return {
            "id": resource.id,
            "name": resource.name,
            "description": resource.description,
            "image": resource.image,
            "default_config": resource.default_config,
            "required_ports": resource.required_ports,
            "created_at": resource.created_at,
            "updated_at": resource.updated_at,
            "volume_path": resource.volume_path
        }, 200

    @staticmethod
    def update_prebuilt_resource_service(resource_id, data):
        resource = PrebuiltResource.query.get(resource_id)
        if not resource:
            return {"error": "Prebuilt resource not found"}, 404

        if 'name' in data:
            resource.name = data['name']
        if 'description' in data:
            resource.description = data['description']
        if 'image' in data:
            resource.image = data['image']
        if 'default_config' in data:
            resource.default_config = data['default_config']
        if 'required_ports' in data:
            resource.required_ports = data['required_ports']
        if 'volume_path' in data:
            resource.volume_path = data['volume_path']

        db.session.commit()
        return {"message": "Prebuilt resource updated successfully"}, 200

    @staticmethod
    def delete_prebuilt_resource_service(resource_id):
        resource = PrebuiltResource.query.get(resource_id)
        if not resource:
            return {"error": "Prebuilt resource not found"}, 404

        db.session.delete(resource)
        db.session.commit()
        return {"message": "Prebuilt resource deleted successfully"}, 200


