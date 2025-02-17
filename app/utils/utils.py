import socket
import random

def get_available_ports(required_ports):
    """
    Assigns free ports on the host machine for each required port in the container.

    Args:
        required_ports (dict): A dictionary where keys are container ports and values are protocols (tcp/udp).
    
    Returns:
        dict: A dictionary mapping container ports (with protocol) to assigned host ports.
    """
    assigned_ports = {}

    for container_port, protocol in required_ports.items():
        # Find an available host port
        host_port = find_free_port(protocol)

        if host_port:
            assigned_ports[f"{container_port}/{protocol}"] = host_port
        else:
            raise Exception(f"Could not find a free port for container port {container_port}/{protocol}")

    return assigned_ports


def find_free_port(protocol):
    """
    Finds an available port on the host machine.

    Args:
        protocol (str): "tcp" or "udp"
    
    Returns:
        int: A free host port number.
    """
    try:
        sock_type = socket.SOCK_STREAM if protocol == "tcp" else socket.SOCK_DGRAM
        with socket.socket(socket.AF_INET, sock_type) as s:
            s.bind(("0.0.0.0", 0))  # Bind to any available port
            s.listen(1) if protocol == "tcp" else None
            return s.getsockname()[1]  # Return assigned port
    except Exception as e:
        print(f"Error finding free port: {e}")
        return None
