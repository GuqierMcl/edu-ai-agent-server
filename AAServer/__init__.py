from django_redis import get_redis_connection

from AAServer.utils.redis_utils import RedisUtil

redis_connect = get_redis_connection()
redis_util = RedisUtil(redis_connect)

import pymysql
pymysql.install_as_MySQLdb()