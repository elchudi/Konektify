import sys
import zmq
import time
import random
import json
import threading



idd = random.randrange(1,1000)
print idd
context = zmq.Context()

# Socket to send messages on
sender = context.socket(zmq.PUSH)
sender.connect("tcp://localhost:5557")

subscriber = context.socket(zmq.SUB)
subscriber.connect("tcp://localhost:5556")
subscriber.setsockopt(zmq.SUBSCRIBE, "")


class Event_sender(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.kill_received = False

    def run(self):
        while not self.kill_received:
            self.do_something()

    def do_something(self):
        press = raw_input("Enter message: ") 
        print press
        t = time.time()
        msg = [idd, t]
        msg = json.dumps(msg)
        sender.send(msg)

class Get_msg(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.kill_received = False

    def run(self):
        while not self.kill_received:
            self.do_something()

    def do_something(self):
        msg = subscriber.recv()
        msg = json.loads(msg)
        print msg

def main():
    threads = []
    t1 = Event_sender()
    t2 = Get_msg()
    threads.append(t1)
    threads.append(t2)
    t1.start()
    t2.start()
    

if __name__ == '__main__':
    main()
