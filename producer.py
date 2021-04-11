from pprint import pprint
import time

from rsmq import RedisSMQ


# Create controller.
# In this case we are specifying the host and default queue name
queue = RedisSMQ(host="127.0.0.1", qname="my-queue")


# Delete Queue if it already exists, ignoring exceptions
queue.deleteQueue().exceptions(False).execute()

# Create Queue with default visibility timeout of 20 and delay of 0
# demonstrating here both ways of setting parameters
queue.createQueue(delay=0).vt(20).execute()


i = 0
try:
    while True:
        i += 1

        # Send a message with a 2 second delay
        message_id = queue.sendMessage().message(f"Hello World {i}").execute()

        pprint({'queue_status': queue.getQueueAttributes().execute()})

        time.sleep(0.1)
        

except KeyboardInterrupt:
    print("ending the work")


# No action
queue.quit()