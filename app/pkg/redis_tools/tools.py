import redis


class RedisTools:
    __redis_connect = redis.Redis(host='localhost', port=6379)

    @classmethod
    def set_pair(cls, pair:str, price: str):
        cls.__redis_connect.set(pair, price)

    @classmethod
    def get_pair(cls, pair):
        return cls.__redis_connect.get(pair)

    @classmethod
    def ger_all_pairs(cls):
        return cls.__redis_connect.keys()

    @classmethod
    def get_keys(cls):
        return cls.__redis_connect.keys(pattern='*')