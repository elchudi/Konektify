from mongrel2 import handler
import zmq
import urllib
import urllib2
import sys
import json

sender_id = "82209006-86FF-4982-B5EA-D1E29E55D481"
conn = handler.Connection(sender_id, "tcp://127.0.0.1:9997", "tcp://127.0.0.1:9996")
context = zmq.Context()

def main(device_to_port, device_from_port):
    while True:
        print "Creating the socket..."
        print "Connecting the socket..."
        device_to_socket = context.socket(zmq.PUSH)
        device_to_socket.connect("tcp://localhost:" + device_to_port)

        device_from_socket = context.socket(zmq.PULL)
        device_from_socket.connect("tcp://localhost:" + device_from_port)

        #Initialize poll set
        poller = zmq.Poller()
        poller.register(device_from_socket, zmq.POLLIN) 
        poller.register(conn.reqs, zmq.POLLIN) 

        while True:
            print "WAITING FOR REQUEST"
            socks = dict(poller.poll())
            if device_from_socket in socks and socks[device_from_socket] == zmq.POLLIN:
                message = device_from_socket.recv()
                message = json.loads(message)
                message =  dict((k.encode('ascii'), v.encode('ascii')) for (k, v) in message.items())
                conn.send(message['uuid'], message['conn_id'], handler.http_response(message['message'], 200, 'OK', {"Access-Control-Allow-Origin": "*"}))
            if conn.reqs in socks and socks[conn.reqs] == zmq.POLLIN:
                req = conn.recv()
                message = {
                    'conn_id' : req.conn_id,
                    'uuid' : req.sender,
                    'message':'mensajee'
                }
                device_to_socket.send(json.dumps(message))

if __name__ == "__main__":
    #main(sys.argv[1], sys.argv[2]) 
    push_port = '5557'
    pull_port = '5556'
    main(push_port, pull_port) 


