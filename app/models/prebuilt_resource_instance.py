from datetime import datetime
from app import db

class PrebuiltResourceInstance(db.Model):
    __tablename__ = 'prebuilt_resource_instances'
    
    id = db.Column(db.Integer, primary_key=True)
    
    # Link to the project that owns this instance
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    
    name = db.Column(db.String(100), nullable=False, default='Instance',server_default='Instance')
    
    # Link to the prebuilt resource type (e.g., MongoDB, Redis)
    resource_id = db.Column(db.Integer, db.ForeignKey('prebuilt_resources.id'), nullable=False)

    # Custom configuration for this instance (overrides default config)
    custom_config = db.Column(db.JSON, nullable=True)
    
    # Assigned ports for this instance (may differ from the default required_ports)
    assigned_ports = db.Column(db.JSON, nullable=False, default={})
    
    assigned_volume_path = db.Column(db.String(255), nullable=True)
    # Deployment status: active, stopped, failed, etc.
    status = db.Column(db.String(50), nullable=False, default='pending')
    
    # environment variables
    environment_variables = db.Column(db.JSON, nullable=True)
    
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f"<PrebuiltResourceInstance {self.id} - {self.status}>"
