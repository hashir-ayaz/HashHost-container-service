# controllers/prebuilt_resource_instance_controller.py
from app import db
from app.models.prebuilt_resource_instance import PrebuiltResourceInstance
from app.models.project import Project
from app.models.prebuilt_resource import PrebuiltResource

def create_instance(data):
    # Validate required fields
    if not data or 'project_id' not in data or 'resource_id' not in data or 'assigned_ports' not in data:
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
        custom_config=data.get('custom_config', {}),
        assigned_ports=data['assigned_ports'],
        status=data.get('status', 'pending')
    )
    db.session.add(new_instance)
    db.session.commit()
    return {"message": "Prebuilt resource instance created successfully", "instance_id": new_instance.id}, 201

def get_all_instances():
    instances = PrebuiltResourceInstance.query.all()
    instance_list = [
        {
            "id": instance.id,
            "project_id": instance.project_id,
            "resource_id": instance.resource_id,
            "custom_config": instance.custom_config,
            "assigned_ports": instance.assigned_ports,
            "status": instance.status,
            "created_at": instance.created_at,
            "updated_at": instance.updated_at
        }
        for instance in instances
    ]
    return instance_list, 200

def get_instance(instance_id):
    instance = PrebuiltResourceInstance.query.get(instance_id)
    if not instance:
        return {"error": "Prebuilt resource instance not found"}, 404

    return {
        "id": instance.id,
        "project_id": instance.project_id,
        "resource_id": instance.resource_id,
        "custom_config": instance.custom_config,
        "assigned_ports": instance.assigned_ports,
        "status": instance.status,
        "created_at": instance.created_at,
        "updated_at": instance.updated_at
    }, 200

def update_instance(instance_id, data):
    instance = PrebuiltResourceInstance.query.get(instance_id)
    if not instance:
        return {"error": "Prebuilt resource instance not found"}, 404

    if 'project_id' in data:
        project = Project.query.get(data['project_id'])
        if not project:
            return {"error": "Project not found"}, 404
        instance.project_id = data['project_id']

    if 'resource_id' in data:
        resource = PrebuiltResource.query.get(data['resource_id'])
        if not resource:
            return {"error": "Prebuilt resource not found"}, 404
        instance.resource_id = data['resource_id']

    if 'custom_config' in data:
        instance.custom_config = data['custom_config']

    if 'assigned_ports' in data:
        instance.assigned_ports = data['assigned_ports']

    if 'status' in data:
        instance.status = data['status']

    db.session.commit()
    return {"message": "Prebuilt resource instance updated successfully"}, 200

def delete_instance(instance_id):
    instance = PrebuiltResourceInstance.query.get(instance_id)
    if not instance:
        return {"error": "Prebuilt resource instance not found"}, 404

    db.session.delete(instance)
    db.session.commit()
    return {"message": "Prebuilt resource instance deleted successfully"}, 200
