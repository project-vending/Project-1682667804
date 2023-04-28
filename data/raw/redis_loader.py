python
import redis

# Create a Redis client and connect to the Redis server
redis_client = redis.Redis(host='localhost', port=6379)

# Open the data file for writing
with open('data/raw/data.txt', 'w') as f:

    # Iterate over all keys in Redis and write the key-value pairs to the file
    for key in redis_client.keys():
        value = redis_client.get(key).decode('utf-8')
        f.write(f'{key.decode("utf-8")}:{value}\n')
        
print("Data loaded from Redis and written to file successfully!")
