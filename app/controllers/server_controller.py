# controllers/server_controller.py
from app.services.server_service import (
    create_server_service,
    get_all_servers_service,
    get_server_service,
    update_server_service,
    delete_server_service
)

def create_server(data):
    return create_server_service(data)

def get_all_servers():
    return get_all_servers_service()

def get_server(server_id):
    return get_server_service(server_id)

def update_server(server_id, data):
    return update_server_service(server_id, data)

def delete_server(server_id):
    return delete_server_service(server_id)
