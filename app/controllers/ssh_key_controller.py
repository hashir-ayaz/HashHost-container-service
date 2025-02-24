from app import db
from ..services.ssh_key_service import SSHKeyService
from ..models.ssh_keys import SSHKey


class SSHKeyController:
    @staticmethod    
    def create_ssh_key(data):
        server_id = data.get('server_id')
        
        serialized_private_key, private_key = SSHKeyService.generate_private_key()
        
        serialized_public_key = SSHKeyService.generate_public_key(private_key)
        
        
        ssh_key = SSHKey(
            server_id=server_id,
            private_key=serialized_private_key,
            public_key=serialized_public_key
        )
        db.session.add(ssh_key)
        db.session.commit()
        
        # TODO fetch the ssh key to store on host computer using id such as ID_rsa
        

        SSHKeyService.save_keys_to_files(serialized_private_key, serialized_public_key)
        return {
            'status': 'success',
            'message': 'SSH key successfully created.'
        }, 201
        
        
    @staticmethod    
    def delete_ssh_key(id):
        ssh_key = SSHKey.query.filter_by(id=id).first()
        if not ssh_key:
            return {
                'status': 'fail',
                'message': 'SSH key does not exist.'
            }, 404
            
        db.session.delete(ssh_key)
        db.session.commit()
        
        return {
            'status': 'success',
            'message': 'SSH key successfully deleted.'
        }, 200
        
    @staticmethod    
    def get_ssh_keys():
        return SSHKey.query.all()

    @staticmethod    
    def get_ssh_key(id):
        return SSHKey.query.filter_by(id=id).first()

    @staticmethod    
    def get_ssh_key_by_server_id(server_id):
        return SSHKey.query.filter_by(server_id=server_id).first()