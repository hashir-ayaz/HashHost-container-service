# controllers/server_controller.py
from app.services.server_service import ServerService
class ServerController:
    @staticmethod    
    def create_server(data):
        return ServerService.create_server_service(data)

    @staticmethod    
    def get_all_servers():
        return ServerService.get_all_servers_service()

    @staticmethod    
    def get_server(server_id):
        return ServerService.get_server_service(server_id)

    @staticmethod    
    def update_server(server_id, data):
        return ServerService.update_server_service(server_id, data)

    @staticmethod    
    def delete_server(server_id):
        return ServerService.delete_server_service(server_id)
