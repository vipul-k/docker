import zmq
import sys
from datetime import datetime
from threading import Thread

def pub_client(HOST, PORT, channel):
    
    server_address = f'tcp://{HOST}:{PORT}'
    context = zmq.Context()
    s = context.socket(zmq.SUB)
    s.connect(server_address)
    s.setsockopt(zmq.SUBSCRIBE, b'')
    count = 0
    while True:
        all_messages = s.recv_pyobj()
        if channel == "ALL":
            count = print_messages(all_messages["ALL"], count)
        elif channel in all_messages:
            count = print_messages(all_messages[channel], count)
        else:
            pass


def print_messages(messages, count):
    if count == 0:
        for i in messages:
            message = i.split(", ")
            print(f"({message[0]}) {message[1]}: {message[3]} ({message[2]})")
            count+=1
    else:
        message = messages[-1].split(", ")
        print(f"({message[0]}) {message[1]}: {message[3]} ({message[2]})")
        
    return count
            
def post_client(HOST, PORT, channel, username):
    
    server_address = f'tcp://{HOST}:{PORT}'
    context = zmq.Context()
    s = context.socket(zmq.REQ)
    s.connect(server_address)
    while True:
        message = input()
        now = datetime.now()
        message_string = f"{channel}, {username}, {now}, {message}"
        s.send_string(message_string)
        _ = s.recv_pyobj()
    
def thread_client(HOST, post_port, pub_port, channel, username):
    
    if channel == "ALL":
        pub_client(HOST, pub_port, channel)
    else:
        threads = []
    
        process1 = Thread(target=post_client, args=[HOST, post_port, channel, username])
        process1.start()
        threads.append(process1)
        process2 = Thread(target=pub_client, args=[HOST, pub_port, channel])
        process2.start()
        threads.append(process2)
        
        for process in threads:
            process.join()
    
    
def main():
    if len(sys.argv) != 6:
        print("Incorrect number of arguments.")
        sys.exit(1)
    ip, post_port, pub_port, channel, username = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], sys.argv[5]

    thread_client(ip, post_port, pub_port, channel, username)
    
if __name__ == "__main__":
    main()
