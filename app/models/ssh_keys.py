from app import db
from datetime import datetime

class SSHKey(db.Model):
    __tablename__ = 'ssh_keys'
    
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(100), nullable=False, default='SSH Key',server_default='SSH Key')
    # Link to the project that owns this SSH key
    server_id = db.Column(db.Integer, db.ForeignKey('servers.id'), nullable=False)
    
    # SSH key in PEM format
    key = db.Column(db.String(4096), nullable=False)
    
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)