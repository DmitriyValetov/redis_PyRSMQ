from rsmq.consumer import RedisSMQConsumer
import time
import datetime

# define Processor
def processor(id, message, rc, ts):
    print(datetime.datetime.now(), 'start')
    time.sleep(1)
    print(message)
    # Do something
    print(datetime.datetime.now(), 'end')
    return True

# create consumer
consumer = RedisSMQConsumer('my-queue', processor, host='127.0.0.1')

# run consumer
consumer.run()