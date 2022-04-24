import zmq
import sys


    
messages = []
def server(HOST, PORT):
    
    server_address = f'tcp://{HOST}:{PORT}'

    context = zmq.Context()
    s = context.socket(zmq.REP)
    s.bind(server_address)
    
    while True:
        message = s.recv_string()
        messages.append(message)
        #s.send_string(messages[0])
                
    
def main():
    if len(sys.argv) != 3:
        print("Incorrect number of arguments.")
        sys.exit(1)
    ip, port = str(sys.argv[1]), int(sys.argv[2])

    
    server(ip, port)
    
if __name__ == "__main__":
    main()