import os
#  isDocker = True if os.environ['USER'] == 'docker' else False
isDocker = True
#  isDocker = False


db_name = 'zoo'
collection_name = 'monkeys'
db_host = 'mongo' if isDocker else None
host_ip = '0.0.0.0' if isDocker else 'localhost'
