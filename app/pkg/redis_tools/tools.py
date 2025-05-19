import redis


class RedisTools:
    __redis_connect = redis.Redis(host='localhost', port=6379)