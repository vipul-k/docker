import zmq
import sys

messages = {"ALL": []}
def server(HOST, post_port, pub_port):
    
    server_address_post = f'tcp://{HOST}:{post_port}'
    server_address_pub = f'tcp://{HOST}:{pub_port}'

    context = zmq.Context()
    s1 = context.socket(zmq.REP)
    s1.bind(server_address_post)
    s2 = context.socket(zmq.PUB)
    s2.bind(server_address_pub)
    
    while True:
        message = s1.recv_string()
        s1.send_pyobj(message)
        messages["ALL"].append(message)
        channel = message.split(", ")[0]
        if channel in messages:
            messages[channel].append(message)
        else:
            messages[channel] = []
            messages[channel].append(message)
        s2.send_pyobj(messages)
                
    
def main():
    if len(sys.argv) != 4:
        print("Incorrect number of arguments.")
        sys.exit(1)
    ip, post_port, pub_port = str(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

    
    server(ip, post_port, pub_port)
    
if __name__ == "__main__":
    main()
