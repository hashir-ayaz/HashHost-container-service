from datetime import datetime
from app import db

class PrebuiltResource(db.Model):
    __tablename__ = 'prebuilt_resources'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    
    # Docker image name or other deployment identifier.
    image = db.Column(db.String(255), nullable=False)
    
    # Default configuration settings for the resource.
    default_config = db.Column(db.JSON, nullable=True)
    
    # Required ports stored as a dictionary, e.g., {"http": 80, "https": 443, "db": 27017}
    required_ports = db.Column(db.JSON, nullable=False, default={})
    
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship: each prebuilt resource can have multiple instances.
    instances = db.relationship('PrebuiltResourceInstance', backref='resource', lazy=True)

    def __repr__(self):
        return f"<PrebuiltResource {self.name}>"
