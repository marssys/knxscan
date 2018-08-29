import sys
import socket
import time

# arguments https://jenyay.net/Programming/Argparse
port_from = 5005 # -p PORT, --port PORT; target UDP port, can be single -p 5000 or range -p 1-65535 (default: 3671)
port_to = 5010
timeout = 2 # -t TIMEOUT, --timeout TIMEOUT; UDP socket timeout (default: 2)
retries = 3 # -r RETRIES, --retries RETRIES; number of description requests (default: 3)
workers = 100 # -w WORKERS, --workers WORKERS; number of threads (default: 100)
# sample: python knxscan.py -p 1-65535 -t 1 -r 1 -w 500 201.21.18.19

if len(sys.argv) == 1:
    print('Target IP address not specified!')
    sys.exit(1)
else:
    ip = sys.argv[1]

# KNX Specification v. 2.1 3/8/2

knx_description_request = b'\x06\x10\x02\x03\x00\x0E\x08\x01\x00\x00\x00\x00\x00\x00'

"""
DESCRIPTION_REQUEST
1 - header size
2 - protocol version
3, 4 - service type identifier 0203h
5, 6 -  total length, 14 octets
7 - structure length
8 - host protocol code, e.g. 01h, for UDP over IPv4
9, 10, 11, 12 -  IP address of control endpoint, e.g. 192.168.200.12
13, 14 - port number of control endpoint, e.g. 50100
"""

"""
DESCRIPTION_RESPONSE
"""

for port in range(port_from, port_to + 1):

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(timeout)
    begin_time = time.time()
    sock.sendto(knx_description_request, (ip, port))

    try:
        data, address = sock.recvfrom(1024)
        print(data)
        print(address)
        print(time.time() - begin_time)
    except socket.timeout:
        print('timeout: ' + str(port))
        print(time.time() - begin_time)

    sock.close()
