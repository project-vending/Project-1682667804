python
import redis

# Create a Redis client
redis_client = redis.Redis(host='localhost', port=6379)

def load_data_to_redis(data):
    """
    Load the transformed data to Redis.
    """
    # Store the data in Redis
    for key, value in data.items():
        redis_client.set(key, value)
