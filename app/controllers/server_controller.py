# controllers/server_controller.py
from app import db
from app.models.server import Server

def create_server(data):
    if not data or 'name' not in data or 'ip_address' not in data:
        return {"error": "Missing required fields"}, 400

    new_server = Server(
        name=data['name'],
        ip_address=data['ip_address'],
        status=data.get('status', 'inactive')
    )
    db.session.add(new_server)
    db.session.commit()
    return {"message": "Server created successfully", "server_id": new_server.id}, 201

def get_all_servers():
    servers = Server.query.all()
    server_list = [
        {"id": server.id, "name": server.name, "ip_address": server.ip_address, "status": server.status}
        for server in servers
    ]
    return server_list, 200

def get_server(server_id):
    server = Server.query.get(server_id)
    if not server:
        return {"error": "Server not found"}, 404
    return {
        "id": server.id,
        "name": server.name,
        "ip_address": server.ip_address,
        "status": server.status
    }, 200

def update_server(server_id, data):
    server = Server.query.get(server_id)
    if not server:
        return {"error": "Server not found"}, 404

    if 'name' in data:
        server.name = data['name']
    if 'ip_address' in data:
        server.ip_address = data['ip_address']
    if 'status' in data:
        server.status = data['status']

    db.session.commit()
    return {"message": "Server updated successfully"}, 200

def delete_server(server_id):
    server = Server.query.get(server_id)
    if not server:
        return {"error": "Server not found"}, 404

    db.session.delete(server)
    db.session.commit()
    return {"message": "Server deleted successfully"}, 200
