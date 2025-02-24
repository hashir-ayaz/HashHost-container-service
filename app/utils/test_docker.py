import docker

client = docker.DockerClient(base_url="tcp://139.59.83.178:2375")
print(client.info())  # Should print VPS Docker details