# services/prebuilt_resource_instance_service.py
from app import db
from app.models.prebuilt_resource_instance import PrebuiltResourceInstance
from app.models.project import Project
from app.models.prebuilt_resource import PrebuiltResource
import docker 

docker_client = docker.from_env()

class PrebuiltResourceInstanceService:
    @staticmethod
    def create_instance_service(data, available_ports):
        if not data or 'project_id' not in data or 'resource_id' not in data or 'assigned_volume_path' not in data:
            return {"error": "Missing required fields"}, 400

        # Ensure the project exists
        project = Project.query.get(data['project_id'])
        if not project:
            return {"error": "Project not found"}, 404

        # Ensure the prebuilt resource exists
        resource = PrebuiltResource.query.get(data['resource_id'])
        if not resource:
            return {"error": "Prebuilt resource not found"}, 404

        new_instance = PrebuiltResourceInstance(
            project_id=data['project_id'],
            resource_id=data['resource_id'],
            name=data.get('name', 'Instance'),
            custom_config=data.get('custom_config'),
            
            # TODO data doesnt have assigned ports to set
            assigned_ports=available_ports,
            status=data.get('status', 'pending'),
            environment_variables=data.get('environment_variables'),
            assigned_volume_path=data.get('assigned_volume_path')
        )
        
        db.session.add(new_instance)
        db.session.commit()
        return {"message": "Prebuilt resource instance created successfully", "instance_id": new_instance.id}, 201

    @staticmethod
    def get_all_instances_service():
        instances = PrebuiltResourceInstance.query.all()
        instance_list = [
            {
                "id": instance.id,
                "project_id": instance.project_id,
                "resource_id": instance.resource_id,
                "name": instance.name,
                "custom_config": instance.custom_config,
                "assigned_ports": instance.assigned_ports,
                "status": instance.status,
                "environment_variables": instance.environment_variables,
                "created_at": instance.created_at.isoformat(),
                "updated_at": instance.updated_at.isoformat()
            }
            for instance in instances
        ]
        return instance_list, 200

    @staticmethod
    def get_instance_service(instance_id):
        instance = PrebuiltResourceInstance.query.get(instance_id)
        if not instance:
            return {"error": "Prebuilt resource instance not found"}, 404

        return {
            "id": instance.id,
            "project_id": instance.project_id,
            "resource_id": instance.resource_id,
            "name": instance.name,
            "custom_config": instance.custom_config,
            "assigned_ports": instance.assigned_ports,
            "status": instance.status,
            "environment_variables": instance.environment_variables,
            "created_at": instance.created_at.isoformat(),
            "updated_at": instance.updated_at.isoformat()
        }, 200

    @staticmethod
    def update_instance_service(instance_id, data):
        instance = PrebuiltResourceInstance.query.get(instance_id)
        if not instance:
            return {"error": "Prebuilt resource instance not found"}, 404

        updatable_fields = [
            'project_id', 'resource_id', 'name', 'custom_config', 
            'assigned_ports', 'status', 'environment_variables'
        ]

        for field in updatable_fields:
            if field in data:
                # Validate foreign keys
                if field == 'project_id':
                    project = Project.query.get(data['project_id'])
                    if not project:
                        return {"error": "Project not found"}, 404
                elif field == 'resource_id':
                    resource = PrebuiltResource.query.get(data['resource_id'])
                    if not resource:
                        return {"error": "Prebuilt resource not found"}, 404
                
                setattr(instance, field, data[field])

        db.session.commit()
        return {"message": "Prebuilt resource instance updated successfully"}, 200

    @staticmethod
    def create_running_instance(data, available_ports):
        # First create the instance in the database
        result, status_code = create_instance_service(data, available_ports)
        if status_code != 201:
            return result, status_code
        
        instance_id = result["instance_id"]
        instance = PrebuiltResourceInstance.query.get(instance_id)
        resource = PrebuiltResource.query.get(instance.resource_id)
        
        if instance.assigned_volume_path:
            container_volume = instance.assigned_volume_path
        else:
            container_volume = resource.volume_path
        try:
            # Run the Docker container
            container_name = f"{instance.name}-{instance.id}"
            container = docker_client.containers.run(
                image=resource.image,
                name=container_name,
                detach=True,
                ports=instance.assigned_ports,
                environment=instance.environment_variables or {},
                volumes={container_name: {'bind': container_volume, 'mode': 'rw'}} 
            )
            
            # Update instance status to active
            instance.status = 'active'
            db.session.commit()
            
            print(f"Container {container.id} is running")
            
            print(container)
            
            return {
                "message": "Instance created and container running",
                "instance_id": instance.id,
                "container_id": container.id
            }, 201
            
        except Exception as e:
            # Update instance status to failed
            print(f"Failed to create container: {str(e)}")
            instance.status = 'failed'
            db.session.commit()
            return {"error": f"Failed to create container: {str(e)}"}, 500

    @staticmethod
    def delete_instance_service(instance_id):
        instance = PrebuiltResourceInstance.query.get(instance_id)
        if not instance:
            return {"error": "Prebuilt resource instance not found"}, 404

        try:
            # Try to stop and remove the container if it exists
            container_name = f"{instance.name}-{instance.id}"
            try:
                container = docker_client.containers.get(container_name)
                container.stop()
                container.remove()
            except docker.errors.NotFound:
                pass  # Container doesn't exist, continue with instance deletion
            
            db.session.delete(instance)
            db.session.commit()
            return {"message": "Instance and container deleted successfully"}, 200
            
        except Exception as e:
            return {"error": f"Failed to delete instance: {str(e)}"}, 500