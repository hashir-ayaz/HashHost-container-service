# services/server_service.py
from app import db
from app.models.server import Server


class ServerService:
    @staticmethod
    def create_server_service(data):
        # Validate required fields
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

    @staticmethod
    def get_all_servers_service():
        servers = Server.query.all()
        server_list = [
            {
                "id": server.id,
                "name": server.name,
                "ip_address": server.ip_address,
                "status": server.status
            }
            for server in servers
        ]
        return server_list, 200

    @staticmethod
    def get_server_service(server_id):
        server = Server.query.get(server_id)
        if not server:
            return {"error": "Server not found"}, 404
        return {
            "id": server.id,
            "name": server.name,
            "ip_address": server.ip_address,
            "status": server.status
        }, 200

    @staticmethod
    def update_server_service(server_id, data):
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

    @staticmethod
    def delete_server_service(server_id):
        server = Server.query.get(server_id)
        if not server:
            return {"error": "Server not found"}, 404

        db.session.delete(server)
        db.session.commit()
        return {"message": "Server deleted successfully"}, 200
