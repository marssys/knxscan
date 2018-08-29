import sys
import socket

if len(sys.argv) == 1:
    print('Port not specified!')
    sys.exit(1)
else:
    UDP_PORT = int(sys.argv[1])

UDP_IP = "127.0.0.1" 

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print("received message:", data)
