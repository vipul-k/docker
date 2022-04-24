import zmq
import sys
from datetime import datetime


def client(HOST, PORT, username, message):
    
    server_address = f'tcp://{HOST}:{PORT}'
    context = zmq.Context()
    s = context.socket(zmq.REQ)
    s.connect(server_address)
    now = datetime.now()
    message_string = f"{username}, {now}, {message}"
    s.send_string(message_string)
    _ = s.recv_pyobj()



def main():
    if len(sys.argv) != 5:
        print("Incorrect number of arguments.")
        sys.exit(1)
    ip, port, username, message = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4]

    client(ip, port, username, message)
    
if __name__ == "__main__":
    main()