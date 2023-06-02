import json
from utils import calculate_execution_time
from RedisCache import RedisCache
from constants import NUMBER_LIST_TEST


REDIS_KEY = 'nums_array'


@calculate_execution_time
def sort_numbers_without_redis(nums):
    return sorted(nums)


@calculate_execution_time
def sort_number_with_redis(key):
    result = redis_client.get_data(key)
    return result


if __name__ == "__main__":
    redis_client = RedisCache()

    result = sort_numbers_without_redis(NUMBER_LIST_TEST)

    redis_client.set_data(REDIS_KEY, json.dumps(result))

    redis_result = sort_number_with_redis(REDIS_KEY)
