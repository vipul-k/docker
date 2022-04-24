import zmq
import sys


def client(HOST, PORT):
    
    server_address = f'tcp://{HOST}:{PORT}'
    context = zmq.Context()
    s = context.socket(zmq.SUB)
    s.connect(server_address)
    s.setsockopt(zmq.SUBSCRIBE, b'')

    count = 0
    while True:
        messages = s.recv_pyobj()
        if count == 0:
            for i in messages:
                message = i.split(", ")
                print(f"{message[0]}: {message[2]} ({message[1]})")
                count+=1
        else:
            message = messages[-1].split(", ")
            print(f"{message[0]}: {message[2]} ({message[1]})")


            
        




def main():
    if len(sys.argv) != 3:
        print("Incorrect number of arguments.")
        sys.exit(1)
    ip, port = sys.argv[1], int(sys.argv[2])

    client(ip, port)
    
if __name__ == "__main__":
    main()





