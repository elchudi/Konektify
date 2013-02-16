import sys
import time
import zmq
import json
context = zmq.Context()

# Socket to receive messages on
receiver = context.socket(zmq.PULL)
receiver.bind("tcp://*:5557")

publisher = context.socket(zmq.PUSH)
publisher.bind("tcp://*:5556")


# Process tasks forever
events = []
delta_time = 0.5
while True:
    print "waiting"
    msg = receiver.recv()
    print "received"
    publisher.send(msg)
    """
    msg = json.loads(msg) 
    events.append(msg)
    print msg
    for e in events:
        for e2 in events:
            if(e[1]!=e2[1]):
                if abs(e[1]-e2[1])< delta_time:
                    publisher.send(json.dumps([e[0],e2[0]]))
    """
