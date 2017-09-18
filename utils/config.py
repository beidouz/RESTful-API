import os

db_name = os.environ['DB_NAME'] if 'DB_NAME' in os.environ else None
collection_name = os.environ['COLLECTION_NAME'] if 'COLLECTION_NAME' in os.environ else None
db_host = os.environ['DB_HOST'] if 'DB_HOST' in os.environ else None
host_ip = os.environ['HOST_IP'] if 'HOST_IP' in os.environ else None
