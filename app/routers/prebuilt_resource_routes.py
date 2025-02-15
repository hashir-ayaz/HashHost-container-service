from flask import Blueprint, request, jsonify
from app import db
from app.models.prebuilt_resource import PrebuiltResource

prebuilt_resource_bp = Blueprint('prebuilt_resource_bp', __name__)  # Define in init.py or run.py

# ===============================
# 📌 CREATE PREBUILT RESOURCE (POST)
# ===============================
@prebuilt_resource_bp.route('/', methods=['POST'])
def create_prebuilt_resource():
    try:
        data = request.get_json()

        if not data or 'name' not in data or 'image' not in data or 'required_ports' not in data:
            return jsonify({"error": "Missing required fields"}), 400

        new_resource = PrebuiltResource(
            name=data['name'],
            description=data.get('description', ""),
            image=data['image'],
            default_config=data.get('default_config', {}),
            required_ports=data['required_ports']
        )
        db.session.add(new_resource)
        db.session.commit()

        return jsonify({"message": "Prebuilt resource created successfully", "resource_id": new_resource.id}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ===============================
# 📌 GET ALL PREBUILT RESOURCES (GET)
# ===============================
@prebuilt_resource_bp.route('/', methods=['GET'])
def get_all_prebuilt_resources():
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
            "updated_at": resource.updated_at
        }
        for resource in resources
    ]
    return jsonify(resource_list), 200

# ===============================
# 📌 GET A SINGLE PREBUILT RESOURCE BY ID (GET)
# ===============================
@prebuilt_resource_bp.route('/<int:resource_id>', methods=['GET'])
def get_prebuilt_resource(resource_id):
    resource = PrebuiltResource.query.get(resource_id)
    if not resource:
        return jsonify({"error": "Prebuilt resource not found"}), 404

    return jsonify({
        "id": resource.id,
        "name": resource.name,
        "description": resource.description,
        "image": resource.image,
        "default_config": resource.default_config,
        "required_ports": resource.required_ports,
        "created_at": resource.created_at,
        "updated_at": resource.updated_at
    }), 200

# ===============================
# 📌 UPDATE PREBUILT RESOURCE (PUT)
# ===============================
@prebuilt_resource_bp.route('/<int:resource_id>', methods=['PUT'])
def update_prebuilt_resource(resource_id):
    resource = PrebuiltResource.query.get(resource_id)
    if not resource:
        return jsonify({"error": "Prebuilt resource not found"}), 404

    try:
        data = request.get_json()

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

        db.session.commit()
        return jsonify({"message": "Prebuilt resource updated successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ===============================
# 📌 DELETE PREBUILT RESOURCE (DELETE)
# ===============================
@prebuilt_resource_bp.route('/<int:resource_id>', methods=['DELETE'])
def delete_prebuilt_resource(resource_id):
    resource = PrebuiltResource.query.get(resource_id)
    if not resource:
        return jsonify({"error": "Prebuilt resource not found"}), 404

    db.session.delete(resource)
    db.session.commit()

    return jsonify({"message": "Prebuilt resource deleted successfully"}), 200
