from datetime import datetime
from app import db

class UserBuiltInstance(db.Model):
    __tablename__ = 'user_built_instances'
    
    id = db.Column(db.Integer, primary_key=True)
    
    # Link to the project that owns this instance
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    
    # Link to the server where this instance is deployed
    server_id = db.Column(db.Integer, db.ForeignKey('servers.id'), nullable=False)
    
    # Docker image provided by the user
    image = db.Column(db.String(255), nullable=False)
    
    # Environment variables (stored as JSON)
    env_vars = db.Column(db.JSON, nullable=True)
    
    # Assigned ports (dict, e.g., {"web": 3000, "api": 8080})
    assigned_ports = db.Column(db.JSON, nullable=False, default={})
    
    # Deployment status: active, stopped, failed, etc.
    status = db.Column(db.String(50), nullable=False, default='pending')
    
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f"<UserBuiltInstance {self.id} - {self.image}>"
