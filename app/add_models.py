import db
from .models.prebuilt_resource import PrebuiltResource

# List of prebuilt resources
resources = [
    PrebuiltResource(
        name="MongoDB",
        description="A source-available cross-platform document-oriented database",
        image="mongo:latest",
        default_config={
            "MONGO_INITDB_ROOT_USERNAME": "admin",
            "MONGO_INITDB_ROOT_PASSWORD": "password123",
            "authentication": "enabled",
            "storage_engine": "wiredTiger"
        },
        required_ports=[27017]
    ),
    
    PrebuiltResource(
        name="PostgreSQL",
        description="Advanced open-source relational database",
        image="postgres:15-alpine",
        default_config={
            "POSTGRES_USER": "postgres",
            "POSTGRES_PASSWORD": "postgres",
            "max_connections": 100,
            "shared_buffers": "128MB",
            "timezone": "UTC"
        },
        required_ports=[5432]
    ),
    
    PrebuiltResource(
        name="Redis",
        description="In-memory data structure store used as cache/message broker",
        image="redis:7-alpine",
        default_config={
            "maxmemory": "256mb",
            "maxmemory-policy": "allkeys-lru",
            "appendonly": "yes"
        },
        required_ports=[6379]
    ),
    
    PrebuiltResource(
        name="MySQL",
        description="Popular open-source relational database management system",
        image="mysql:8",
        default_config={
            "MYSQL_ROOT_PASSWORD": "rootpass",
            "MYSQL_DATABASE": "myapp",
            "max_connections": 151,
            "character-set-server": "utf8mb4",
            "collation-server": "utf8mb4_unicode_ci"
        },
        required_ports=[3306]
    ),
    
    PrebuiltResource(
        name="Elasticsearch",
        description="Distributed search and analytics engine",
        image="elasticsearch:8.7.0",
        default_config={
            "discovery.type": "single-node",
            "ES_JAVA_OPTS": "-Xms512m -Xmx512m",
            "xpack.security.enabled": "false"
        },
        required_ports=[9200, 9300]
    ),

    PrebuiltResource(
        name="CassandraDB",
        description="Highly-scalable NoSQL database",
        image="cassandra:latest",
        default_config={
            "MAX_HEAP_SIZE": "512M",
            "HEAP_NEWSIZE": "100M",
            "CASSANDRA_CLUSTER_NAME": "MyCluster"
        },
        required_ports=[7000, 7001, 7199, 9042, 9160]
    )
]

# Add to database
def add_resources():
    for resource in resources:
        try:
            db.session.add(resource)
            db.session.commit()
            print(f"Added {resource.name}")
        except Exception as e:
            db.session.rollback()
            print(f"Error adding {resource.name}: {str(e)}")

# Call the function
add_resources()