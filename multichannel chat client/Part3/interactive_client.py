import zmq
import sys
from datetime import datetime
from threading import Thread


def client(HOST, post_port, pub_port, username):
    
    server_address_post = f'tcp://{HOST}:{post_port}'
    server_address_pub = f'tcp://{HOST}:{pub_port}'
    context = zmq.Context()
    s1 = context.socket(zmq.REQ)
    s1.connect(server_address_post)
    s2 = context.socket(zmq.SUB)
    s2.connect(server_address_pub)
    s2.setsockopt(zmq.SUBSCRIBE, b'')

    while True:
        message = input()
        now = datetime.now()
        message_string = f"{username}, {now}, {message}"
        s1.send_string(message_string)
        s1.recv_pyobj()
        recv_message = s2.recv_pyobj()
      
        for i in recv_message:
            message = i.split(", ")
            print(f"{message[0]}: {message[2]} ({message[1]})")




def main():
    if len(sys.argv) != 5:
        print("Incorrect number of arguments.")
        sys.exit(1)
    ip, post_port, pub_port, username = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]

    client(ip, post_port, pub_port, username)
    
if __name__ == "__main__":
    main()

