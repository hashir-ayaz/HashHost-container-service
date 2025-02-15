from datetime import datetime
from app import db  # Assuming your SQLAlchemy instance is defined in app/__init__.py

class Server(db.Model):
    __tablename__ = 'servers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    ip_address = db.Column(db.String(45), nullable=False)  # Supports IPv4 and IPv6
    status = db.Column(db.String(50), nullable=False, default='inactive')  # e.g., active, inactive, maintenance
    # api_token = db.Column(db.String(255), nullable=True)  # Optional: for API interactions or secure access

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship: a server can have multiple projects.
    projects = db.relationship('Project', backref='server', lazy=True)

    def __repr__(self):
        return f"<Server {self.name} ({self.ip_address})>"
