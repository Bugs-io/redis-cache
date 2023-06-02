import redis


class RedisCache:
    def __init__(self, host='localhost', port=6379, password=None):
        self.redis_client = redis.Redis(
                host=host,
                port=port,
                password=password,
                decode_responses=True
                )

    def get_data(self, key):
        if self.redis_client.exists(key):
            data = self.redis_client.get(key)
            return data
        return None

    def set_data(self, key, data):
        self.redis_client.set(key, data)
