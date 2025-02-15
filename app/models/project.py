from datetime import datetime
from app import db  # Assuming your SQLAlchemy instance is defined in app/__init__.py

class Project(db.Model):
    __tablename__ = 'projects'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    
    # Link to the server where the project is hosted
    server_id = db.Column(db.Integer, db.ForeignKey('servers.id'), nullable=False)
    
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships:
    # This assumes you'll create a PrebuiltResourceInstance model later to link a project to its prebuilt resources.
    prebuilt_resources_instances = db.relationship('PrebuiltResourceInstance', backref='project', lazy=True)
    
    # You can also add a relationship for user-built resources:
    user_built_instances = db.relationship('UserBuiltInstance', backref='project', lazy=True)

    def __repr__(self):
        return f"<Project {self.name}>"
