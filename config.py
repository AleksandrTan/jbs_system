# redis
import os

REDIS_HOST = 'localhost'
REDIS_PORT = 6379

# rabbitMQ
RABBIT_HOST = os.getenv('RABBIT_HOST', default='localhost')
RABBIT_PORT = os.getenv('RABBIT_PORT', default=5672)
QUEUE_NAME = os.getenv('QUEUE_NAME', default="jobspamer")

# NySQL
MYSQL_USER = "root"
MYSQL_PASSWORD = "ufeltfvec"
MYSQL_HOST = "localhost"
DB_NAME = "job_board_scrapper"
MYSQL_CONNECT = "mysql://root:ufeltfvec@localhost/job_board_scrapper"
