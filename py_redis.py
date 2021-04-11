import redis

# connect to redis
# client = redis.Redis(host='localhost', port=6379)
client = redis.Redis(host='192.168.99.101', port=6379)

# set a key
client.set('test-key', 'test-value')

# get a value
value = client.get('test-key')
print(value)

client.delete('test-key')