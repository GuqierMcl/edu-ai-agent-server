from django_redis import get_redis_connection
redis_connect = get_redis_connection()

import pymysql
pymysql.install_as_MySQLdb()